from django.urls import path
from .views import index, tambah_karyawan
from django.contrib.auth import views as auth_views 
from gajianApp import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('tempates/tambah',views.tambah_karyawan, name = 'tambah_karyawan'),
    path('daftar/', views.daftar_karyawan, name='daftar_karyawan'),
    
     # URL untuk halaman login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # URL untuk halaman logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('karyawan/casual/', views.daftar_karyawan, name='karyawan_casual'),
]