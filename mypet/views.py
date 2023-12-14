from mypet.models import MyUser
from django.contrib.auth import logout
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


def logout_view(request):
    logout(request)
    return redirect('home')

def posts(request):
   AN =annonce.objects.all()
   context={'Annonces': AN}
     # Retrieve all  objects from the database
   return render(request, 'posts.html', context)
   

def menu(request):  
   # x={'name':'dounia','age':'21'}
   return render(request,'menu.html')
def info(request):
   # x={'name':'dounia','age':'21'}
   return render(request,'info.html')
from .forms import MyUser

def annonces(request):
    if request.user.is_authenticated:
        AN = annonce.objects.filter(user=request.user)
        A = annonce.objects.filter(user=request.user).values_list('id', flat=True).first()
        context = {'ANN': AN, 'A': A}
        return render(request, 'annonces.html', context)





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


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
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


from .models import annonce
from django.contrib import messages

def addAn(request):
    if request.method == "POST":
        prod = annonce()
        if request.user.is_authenticated:
         prod.user=request.user
         prod.nom_animal= request.POST.get('animalname')
         prod.age= request.POST.get('age')
         prod.race = request.POST.get('race')
         prod.espece = request.POST.get('espece')
         prod.sex = request.POST.get('sex')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image1']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('annonces')
    return render(request, 'annonces.html')


def AN_table(request):
   AN =annonce.objects.all()
   US=MyUser.objects.all()
   context={'Annonces': AN ,'user':US}
     # Retrieve all  objects from the database
   return render(request, 'table.html', context)

def modifier(request,annonce_id):
   AN  = annonce.objects.get(id=annonce_id)
   context={'an': AN}
    # Retrieve all  objects from the database
   return render(request, 'modify.html',context)

#def details(request,annonce_id):
  # AN  = Annonce.objects.get(id=annonce_id)
  # context={'an': AN}
    # Retrieve all  objects from the database
   #return render(request, 'test.html',context)


from .models import annonce



def delete_row(request,row_id):
    # Retrieve the object you want to delete
   try:
    annonce.objects.get(id=row_id).delete()
    
   
    return redirect('annonces')
   except annonce.DoesNotExist:
        # Handle the case where the Annonce object with the provided id does not exist
        # Redirect to an error page or display an error message
        return redirect('annonces')

  
from django.shortcuts import render,  redirect
from .models import annonce

def modify_row(request, annonce_id):
    # Fetch the specific Annonce object to modify
    Annonce = annonce.objects.get(id=annonce_id)

    if request.method == 'POST':
        # Retrieve the modified data from the form
        nom_animal = request.POST['nameanimal']
        espece = request.POST['espece']
        race = request.POST['race']
        age = int(request.POST['age'])
        sex = request.POST['sex']

        # Update the fields of the Annonce object
        Annonce.nom_animal = nom_animal
        Annonce.espece = espece
        Annonce.race = race
        Annonce.age = age
        Annonce.sex = sex

        # Save the modified object
        Annonce.save()

        # Redirect to a success page or another view
        return redirect('annonces')

    # Render the form with the existing data for modification
     
 

def mypet_details(request, id):
    # Retrieve the Annonce object with related user information
    Annonce = annonce.objects.select_related('user').get(id=id)
    
    context = {
        'annonce': Annonce,
        # Other context data
    }
    
    return render(request, 'test.html', context)