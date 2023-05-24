from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('Register',views.Register,name='Register'),
    path('home',views.home,name='home'),
    path('user_table',views.user_table, name='user_table'),
    path('posts',views.posts,name='posts'),
    path('menu',views.menu,name='menu'),
    path('register',views.register,name='register'),
    path('info',views.info,name='info'),
    path('annonces',views.annonces,name='annonces'),
    path('Accueil',views.Acceuil,name='Accueil'),



]
