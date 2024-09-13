from django.urls import path
from .views import index, tambah_karyawan,post_karyawan
from django.contrib.auth import views as auth_views 
from gajianApp import views


urlpatterns = [
    path('index', index, name='index'),
    path('tambah_karyawan', tambah_karyawan, name = 'tambah_karyawan'),
    path('post_karyawan', post_karyawan, name='post_karyawan'),
    
     # URL untuk halaman login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # URL untuk halaman logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('karyawan/casual/', views.casual_karyawan, name='casual_karyawan'),
]