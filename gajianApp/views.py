from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tambah_karyawan(request):
    return render(request, 'tambah-karyawan.html')

def post_karyawan(request):
    if request.method == 'POST':
        karyawanid = request.POST.get('karyawanid')
        if karyawanid:
            # Jika ada karyawanid, lanjutkan proses.
            messages.success(request, 'Karyawan berhasil ditambahkan!')
            return HttpResponse(f"Karyawan ID: {karyawanid}")
        else:
            # Jika karyawanid tidak ada, berikan pesan kesalahan.
            messages.error(request, 'Karyawan ID tidak boleh kosong!')
            return redirect('tambah_karyawan')
    else:
        # Jika request bukan POST, kembalikan ke halaman tambah_karyawan
        return redirect('tambah_karyawan')
    
from django.shortcuts import render

def casual_karyawan(request):
    return render(request, 'karyawan/casual.html')

