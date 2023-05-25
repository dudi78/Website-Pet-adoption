from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect





# Create your views here.
def home(request):
   # x={'name':'dounia','age':'21'}
    return render(request,'sm.html')

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



def Acceuil(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'Accueil.html')




from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def  login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


from .models import Annonce

def create_annonce(request):
    if  request.method == 'POST':
        nom_animal = request.POST.get('animalname')
        espece = request.POST.get('prix')
        race = request.POST.get('race')
        age = request.POST.get('age')
        sexe = request.POST.get('sexe')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')

        # Create a new Annonce object and save it to the database
        annonce = Annonce(nom_animal=nom_animal, espece=espece, race=race, age=age, sexe=sexe,
                          image1=image1, image2=image2, image3=image3)
        annonce.save()

        # Redirect to a success page or wherever you want
        return redirect('menu')

    return render(request, 'annonces.html')
