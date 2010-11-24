# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

def category(request):
	try:
		return {'category': request.category}
	except AttributeError:
		return {}
