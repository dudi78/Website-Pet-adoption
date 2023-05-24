from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect




# Create your views here.
def home(request):
   # x={'name':'dounia','age':'21'}
    return render(request,'sm.html')
def register(request):
   # x={'name':'dounia','age':'21'}
    return render(request,'linterfacelogin.html')

def posts(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'posts.html')

def menu(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'menu.html')
def info(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'info.html')
def annonces (request):
   # x={'name':'dounia','age':'21'}
   return render(request,'annonces.html')
def user_table(request):
   users = User.objects.all()  # Retrieve all user objects from the database
   return render(request, 'table.html', {'users': users})


def Acceuil(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'Accueil.html')



from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Perform login logic here
        return redirect('menu')
    return render(request, 'linterfacelogin.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        tel = request.POST['tel']
        email = request.POST['email']
        user = User(username=username, password=password, lastname=lastname, firstname=firstname, tel=tel, email=email)
        user.save()
        # Perform registration logic here
        return redirect('menu')
    return render(request, 'linterfacelogin.html')

