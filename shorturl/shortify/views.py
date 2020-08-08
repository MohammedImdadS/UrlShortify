from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Urltab
from .forms import Urlform
# Create your views here.

def home(request):
	if request.method == "POST":
		form = Urlform(request.POST)
		if form.is_valid():
			new_url = form.cleaned_data.get("longurl")
			obj,create = Urltab.objects.get_or_create(longurl = new_url)
			context = {
			     # "form":form,
			     "obj":obj,
			 }
			if create:
				return render(request,'shortify/created.html',context)
			else:
				return render(request,'shortify/existed.html',context)
	form = Urlform()
	return render(request,'shortify/home.html',{'form':form})


def transferurl(request,shorturl,*args,**kwargs):
	obj = get_object_or_404(Urltab, shorturl = shorturl)
	return HttpResponseRedirect(obj.longurl)
