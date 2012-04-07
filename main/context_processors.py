# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

def category(request):
	try:
		return {'category': request.category}
	except AttributeError:
		return {}
