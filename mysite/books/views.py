from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You search for %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
