from django.urls import path
from .views import index, tambah_karyawan,post_karyawan

urlpatterns = [
    path('index', index, name='index'),
    path('tambah_karyawan', tambah_karyawan, name = 'tambah_karyawan'),
    path('post_karyawan', post_karyawan, name='post_karyawan')
]