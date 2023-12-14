from django.urls import path
from . import views
urlpatterns = [
   
    
    path('home',views.home,name='home'),
    path('posts',views.posts,name='posts'),
    path('menu',views.menu,name='menu'),
    path('mypet_details/<int:id>',views.mypet_details,name='mypet_details'),
    path('info',views.info,name='info'),
    path('annonces',views.annonces,name='annonces'), 
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('addAN', views.addAn, name="addAN"), 
    path('AN_table', views.AN_table, name="AN_table"),
    path('delete_row/<int:row_id>',views.delete_row, name='delete_row'),
    path('modify_row/<int:annonce_id>', views.modify_row, name='modify_row'),
    path('modifier/<int:annonce_id>', views.modifier, name='modifier'),
    path('logout', views.logout_view, name='logout'),
    


]

