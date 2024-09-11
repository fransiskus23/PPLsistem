from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tambah_karyawan(request):
    return render(request, 'tambah-karyawan.html')

def post_karyawan(request):
    karyawanid = request.POST['karyawanid']
    return HttpResponse(karyawanid)