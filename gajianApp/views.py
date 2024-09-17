from django.shortcuts import render, redirect
from .models import KaryawanCasual
from .forms import KaryawanCasualForm

def tambah_karyawan(request):
    if request.method == 'POST':
        form = KaryawanCasualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_karyawan')  # Redirect ke halaman daftar karyawan
    else:
        form = KaryawanCasualForm()
    
    return render(request, 'tambah_karyawan.html', {'form': form})

def daftar_karyawan(request):
    karyawan_list = KaryawanCasual.objects.all()
    return render(request, 'daftar_karyawan.html', {'karyawan_list': karyawan_list})

def index(request):
    return render(request, 'index.html')

