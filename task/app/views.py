from django.shortcuts import render,redirect
from .models import *


def page1(request):
  context = {}
  return render(request, "app/page1.html")

def add_page1(request):

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		contact = request.POST['contact']
		age = request.POST['age']

	Intro.objects.create(name=name,email=email,contact=contact,age=age)
	return redirect('view_intro')
  
def view_intro(request):

    intro = Intro.objects.all()
    context = {'result':intro}
    return render(request, 'app/view_intro.html', context)
