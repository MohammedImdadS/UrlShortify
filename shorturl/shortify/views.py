from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Urltab,User_account
from .forms import Urlform
# Create your views here.

def home(request):
	if request.method == "POST":
		form = Urlform(request.POST)
		if form.is_valid():
			new_url = form.cleaned_data.get("longurl")
			obj,create = Urltab.objects.get_or_create(longurl = new_url)
			context = {
			     "obj":obj,
			 }
			if create:
				if request.user.is_authenticated:
					user_id = request.user.id
					user_inst = User.objects.get(pk = user_id )
					value,crt=User_account.objects.get_or_create(user=user_inst)
					value.url.add(obj)
					value.save()
				return render(request,'shortify/created.html',context)
			else:
				if request.user.is_authenticated:
					user_id = request.user.id
					user_inst = User.objects.get(pk = user_id )
					value,crt=User_account.objects.get_or_create(user=user_inst)
					value.url.add(obj)
					value.save()
				return render(request,'shortify/existed.html',context)
	form = Urlform()
	return render(request,'shortify/home.html',{'form':form})


def transferurl(request,shorturl,*args,**kwargs):
	obj = get_object_or_404(Urltab, shorturl = shorturl)
	return HttpResponseRedirect(obj.longurl)


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	form = UserRegisterForm()
	return render(request, 'shortify/register.html',{'form':form})


@login_required
def my_account(request):
	user_id = request.user.id
	user = User_account.objects.get(user=user_id)
	urllist = user.url.all()
	return render(request,'shortify/my_account.html',{'urllist':urllist})

