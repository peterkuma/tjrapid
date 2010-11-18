def category(request):
	try:
		return {'category': request.category}
	except AttributeError:
		return {}
