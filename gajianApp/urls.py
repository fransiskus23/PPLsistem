from django.urls import path
from .views import index, tambah_karyawan, tambah_presensi
from django.contrib.auth import views as auth_views 
from gajianApp import views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('index/', views.index, name='index'),
    path('tambah/', tambah_karyawan, name='tambah_karyawan'),
    path('daftar/', views.daftar_karyawan, name='daftar_karyawan'),
    
    # URL untuk halaman logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('karyawan/casual/', views.daftar_karyawan, name='karyawan_casual'),

    # Route untuk halaman presensi
    path('presensi/', views.presensi, name='presensi'),

    path('slipGaji/', views.slip_gaji_view, name='slipGaji'),

    path('itemGaji/', views.item_gaji_list, name='itemGaji'),

    path('tambah_presensi', tambah_presensi, name='tambah_presensi')
]
