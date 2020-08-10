from django.urls import path,re_path
from shortify.views import register,home,transferurl,my_account
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
		path('',home, name = 'home'),
		path('login',LoginView.as_view(template_name ='shortify/login.html'),name='login'),
		path('logout',LogoutView.as_view(template_name ='shortify/logout.html'), name='logout'),
		path('register',register, name = 'register'),
		path('my_account',my_account, name = 'my_account'),
		re_path(r'^(?P<shorturl>[\w-]+)/$',transferurl,name = 'directing'),
]