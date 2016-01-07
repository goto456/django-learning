#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: views.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.01.06
#########################################################################

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import ContactForm

#def contact(request):
#    errors = []
#    if request.method == 'POST':
#        if not request.POST.get('subject', ''):
#            errors.append('Enter a subject.')
#        if not request.POST.get('message', ''):
#            errors.append('Enter a message.')
#        if request.POST.get('email') and '@' not in request.POST['email']:
#            errors.append('Enter a valid e-mail address.')
#        if not errors:
#            send_mail(
#                    request.POST['subject'], 
#                    request.POST['message'], 
#                    request.POST.get('email', 'noreply@example.com'), 
#                    ['wangbiwen_88@qq.com']
#                    )
#            return HttpResponseRedirect('/contact/thanks/')
#    return render_to_response('contact_form.html', {
#        'errors': errors,
#        'subject': request.POST.get('subject', ''),
#        'message': request.POST.get('message', ''),
#        'email': request.POST.get('email', ''),
#        })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # do something
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site'})
        #form = ContactForm({'subject': 'I love your site'})
    return render_to_response('contact_form.html', {'form': form})



def thanks(request):
    return render_to_response('contact_success.html')
            
