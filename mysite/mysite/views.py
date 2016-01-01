#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: views.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2015.12.31
#########################################################################

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
#from django.http import Http404
from django.shortcuts import render_to_response

import datetime

def hello(request):
    return HttpResponse("Hello world")

"""
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({'current_date': now})
    d = {'current_date': now}
    html = t.render(d)
    #html = t.render(c)
    #html =  "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
"""
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html =  "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt) 
    ##assert False
    return HttpResponse(html)
