from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('posts',views.posts,name='posts'),
    path('menu',views.menu,name='menu'),
    path('info',views.info,name='info'),
    path('annonces',views.annonces,name='annonces'),
    path('Accueil',views.Acceuil,name='Accueil'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),




]
