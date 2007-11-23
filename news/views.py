from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils import translation
from django import newforms as forms
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

from datetime import date

from tjrapid import settings
from tjrapid.main.models import *
from models import *

def archive(request,category,lang=settings.LANGUAGE_CODE,year=None,month=None,day=None,id=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	c = Category.objects.get(language__code=lang,name=category)
	a = Article.objects.filter(category=c)
	
	if year: a = a.filter(published__year=year)
	if month: a = a.filter(published__month=month)
	if day: a = a.filter(published__day=day)	

	if month:
		if int(month) <= 12 and int(month) >= 1:
			month_name = date(1980,int(month),1).strftime('%B')
		else:
			raise Http404
	else:
		month_name = None

	location = []
	if year: location += [{ 'name': 'News', 'url': c.get_absolute_url()+'news/' }]
	if month: location += [{ 'name': year, 'url': c.get_absolute_url()+'news/'+year+'/' }]
	if day:
		location += [{ 'name': month_name, 'url': c.get_absolute_url()+'news/'+year+'/'+month+'/' }]
	
	return render_to_response(
		'news/archive/'+c.template_name, {
			'category': c,
			'articles': a,
			'location': location,
			'year': year,
			'month': month,
			'month_name': month_name,
			'day': day,
		},
		RequestContext(request)
	)

def details(request,category,lang=settings.LANGUAGE_CODE,year=None,month=None,day=None,id=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	try:
		c = Category.objects.get(language__code=lang,name=category)
		a = Article.objects.get(category=c,published__year=year, \
			published__month=month,published__day=day,id=id)
	except ObjectDoesNotExist:
		raise Http404

	location = (
		{ 'name': _('News'), 'url': c.get_absolute_url()+'news/' },
		{ 'name': a.published.strftime('%Y'), 'url': c.get_absolute_url()+'news/'+a.published.strftime('%Y')+'/' },
		{ 'name': a.published.strftime('%B'), 'url': c.get_absolute_url()+'news/'+a.published.strftime('%Y')+'/'+a.published.strftime('%m')+'/' },
	)

	def comments_recur(objects,reply=None,level=0):
		out = []
		if reply != None:
			layer = objects.filter(reply=reply)
		else:
			layer = objects.filter(reply__isnull=True)
		for o in layer:
			out += [{'comment':o,'level':level}] + comments_recur(objects,o,level+1)
		return out
	
	comments = comments_recur(Comment.objects.filter(article=a))
	
	return render_to_response(
		'news/details/'+c.template_name, {
			'category': c,
			'article': a,
			'location': location,
			'comments': comments,
		},
		RequestContext(request)
	)

def comment(request,category,lang=settings.LANGUAGE_CODE,year=None,month=None,day=None,id=None,reply_id=None):
	try:
		c = Category.objects.get(language__code=lang,name=category)
		a = Article.objects.get(category=c,published__year=year, \
			published__month=month,published__day=day,id=id)
	except ObjectDoesNotExist:
		raise Http404
		
	try:
		reply = Comment.objects.get(id=reply_id)
		initial_subject = 'Re: %s' % reply.subject
	except ObjectDoesNotExist:
		reply = None
		initial_subject = None

	class CommentForm(forms.Form):
		subject = forms.CharField(max_length=100,initial=initial_subject,
			widget=forms.TextInput(attrs={'size':'40'}))
		message = forms.CharField(max_length=300,widget=forms.Textarea())
		sender = forms.CharField(max_length=50)
	
	comment = None
	if request.method == 'POST':
		f = CommentForm(request.POST)
		if f.is_valid():
			comment = Comment(
				article = a,
				reply = reply,
				subject = f.cleaned_data['subject'],
				message = f.cleaned_data['message'],
				sender = f.cleaned_data['sender']
			)
			if request.POST.has_key('send'):
				comment.save()
				return HttpResponseRedirect(a.get_absolute_url())

	else:
		f = CommentForm()

	return render_to_response(
		'news/comment/'+c.template_name, {
			'category': c,
			'article': a,
			'reply': reply,
			'comment': comment,
			'form': f,
		},
		RequestContext(request)
	)
