from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import KaryawanCasual, Presensi, SlipGaji, ItemGaji
from .forms import KaryawanCasualForm, LoginForm, PresensiForm  

def tambah_presensi(request):
    if request.method == 'POST':
        form = PresensiForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data presensi ke database
            messages.success(request, 'Data presensi berhasil disimpan!')
            return redirect('presensi')  # Pastikan URL 'presensi' sesuai dengan nama di urls.py
        else:
            messages.error(request, 'Data presensi gagal disimpan!')
    else:
        form = PresensiForm()
    
    return render(request, 'tambah_presensi.html', {'form': form})

def tambah_karyawan(request):
    if request.method == 'POST':
        form = KaryawanCasualForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan data ke database
            messages.success(request, 'Data karyawan berhasil disimpan.')
            return redirect('daftar_karyawan')  
        else:
            messages.error(request, 'Gagal menyimpan data. Periksa form dan coba lagi.')
    else:
        form = KaryawanCasualForm()

    context = {'form': form}
    return render(request, 'tambah_karyawan.html', context)
    

def daftar_karyawan(request):
    karyawan_list = KaryawanCasual.objects.all()
    return render(request, 'daftar_karyawan.html', {'karyawan_list': karyawan_list})

from django.shortcuts import render
from .models import Presensi  # sesuaikan dengan model Anda

def presensi(request):
    presensi_list = Presensi.objects.select_related('karyawan').all()  # Menggunakan select_related untuk optimalisasi query
    return render(request, 'presensi.html', {'presensi_list': presensi_list})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Otentikasi pengguna
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # arahkan ke halaman home setelah login
        else:
            messages.error(request, 'Username atau password salah.')
    
    return render(request, 'registration/login.html')

def index(request):
    return render(request, 'index.html')

def slip_gaji_view(request):
    slip_gaji_list = SlipGaji.objects.all()
    return render(request, 'slipGaji.html', {'slip_gaji_list': slip_gaji_list})

def item_gaji_list(request):
    item_gaji_list = ItemGaji.objects.all()
    return render(request, 'itemGaji.html', {'item_gaji_list': item_gaji_list})

        