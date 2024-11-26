from django.contrib.auth.models import User
from django.db import models

class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama_jabatan = models.CharField(max_length=100)
    gaji_pokok = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.nama_jabatan


from django.contrib.auth.models import User

class KaryawanCasual(models.Model):
    id_karyawan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    ttl = models.DateField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    tgl_bergabung = models.DateField()
    jabatan = models.ForeignKey('Jabatan', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Relasi ke auth_user

    def __str__(self):
        return self.nama

    def create_auth_user(self, password):
        """
        Sinkronisasi data karyawan ke tabel auth_user.
        """
        if not self.user:  # Hanya buat user jika belum ada
            user = User.objects.create_user(username=self.nama, email=self.email, password=password)
            user.first_name = self.nama.split(" ")[0]  # Nama depan
            user.last_name = " ".join(self.nama.split(" ")[1:])  # Nama belakang (opsional)
            user.save()
            self.user = user
            self.save()
        return self.user

    def validate_login(self, username, password):
        """
        Validasi login menggunakan model User.
        """
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        return user


class Presensi(models.Model):
    id_presensi = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('hadir', 'Hadir'),
            ('tidak hadir', 'Tidak Hadir'),
            ('cuti', 'Cuti'),
            ('sakit', 'Sakit')
        ]
    )
    karyawan = models.ForeignKey(KaryawanCasual, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.karyawan.nama} - {self.tanggal}"


class MasterGaji(models.Model):
    id_master_gaji = models.AutoField(primary_key=True)
    komponen_gaji = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def _str_(self):
        return self.komponen_gaji


class SlipGaji(models.Model):
    id_slip_gaji = models.AutoField(primary_key=True)
    karyawan = models.ForeignKey(KaryawanCasual, on_delete=models.CASCADE)
    periode = models.CharField(
        max_length=20,
        choices=[
            ('minggu', 'Minggu'),
            ('bulan', 'Bulan'),
            ('tahun', 'Tahun')
        ]
    )
    total_gaji = models.DecimalField(max_digits=12, decimal_places=2)

    def _str_(self):
        return f"Slip Gaji {self.karyawan.nama} - {self.periode}"


class ItemGaji(models.Model):
    id_item_gaji = models.AutoField(primary_key=True)
    slip_gaji = models.ForeignKey(SlipGaji, on_delete=models.CASCADE)
    jenis_item = models.CharField(
        max_length=50,
        choices=[
            ('gaji_pokok', 'Gaji Pokok'),
            ('bonus', 'Bonus'),
            ('pinjaman', 'Pinjaman'),
            ('potongan', 'Potongan')
        ]
    )
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)

    def _str_(self):
        return f"{self.jenis_item} - {self.jumlah}"