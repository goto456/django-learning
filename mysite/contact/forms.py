#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: forms.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.01.06
#########################################################################

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

