from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import KaryawanCasual, Presensi, SlipGaji, ItemGaji
from .forms import KaryawanCasualForm, LoginForm, PresensiForm  
from django import forms

def tambah_presensi(request):
    if request.method == 'POST':
        # Ambil data dari form
        karyawan_id = request.POST.get('karyawan')
        status = request.POST.get('status')

        # Validasi input
        if not karyawan_id or not status:
            messages.error(request, 'Semua field harus diisi!')
        else:
            try:
                # Cek apakah karyawan ada
                karyawan = KaryawanCasual.objects.get(id=karyawan_id)
                
                # Cek apakah presensi sudah ada untuk hari ini
                if Presensi.objects.filter(karyawan=karyawan, tanggal=date.today()).exists():
                    messages.error(request, f"Presensi untuk {karyawan.nama} pada hari ini sudah ada!")
                else:
                    # Simpan presensi
                    Presensi.objects.create(
                        karyawan=karyawan.nama,
                        tanggal=date.today(),
                        status=status
                    )
                    messages.success(request, f'Presensi untuk {karyawan.nama} berhasil ditambahkan!')
                    return redirect('presensi')  # Ganti dengan URL halaman presensi
            except KaryawanCasual.DoesNotExist:
                messages.error(request, 'Karyawan tidak ditemukan!')
    
    # Ambil semua karyawan untuk dropdown
    karyawan_list = KaryawanCasual.objects.all()
    return render(request, 'tambah_presensi.html', {'karyawan_list': karyawan_list})

def tambah_karyawan(request):
    if request.method == 'POST':
        form = KaryawanCasualForm(request.POST)
        if form.is_valid():
            form.save() 
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
from .models import Presensi 

def presensi(request):
    presensi_list = Presensi.objects.select_related('karyawan').all()  # Menggunakan select_related untuk optimalisasi query
    return render(request, 'presensi.html', {'presensi_list': presensi_list})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nama Karyawan")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

# View untuk login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Autentikasi pengguna
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Arahkan ke dashboard setelah login
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def slip_gaji_view(request):
    slip_gaji_list = SlipGaji.objects.all()
    return render(request, 'slipGaji.html', {'slip_gaji_list': slip_gaji_list})

def item_gaji_list(request):
    item_gaji_list = ItemGaji.objects.all()
    return render(request, 'itemGaji.html', {'item_gaji_list': item_gaji_list})

        