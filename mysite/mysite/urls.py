"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from views import hello
from views import current_datetime
from views import hours_ahead
from views import current_url_view_good
from views import display_meta
from views import display_meta_template
#from books import views
#from contact import views
from books.views import search
from contact.views import contact, thanks


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^request/$', current_url_view_good),
    url(r'^meta/$', display_meta),
    url(r'^meta2/$', display_meta_template),
    #url(r'^search-form/$', views.search_form),
    #url(r'^search/$', views.search),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks),
]
