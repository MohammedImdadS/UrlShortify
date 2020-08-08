from django.urls import path,re_path
from shortify import views

urlpatterns = [
		path('',views.home, name = 'home'),
		re_path(r'^(?P<shorturl>[\w-]+)/$',views.transferurl)
]