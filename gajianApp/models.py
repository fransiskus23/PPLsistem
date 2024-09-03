from django.db import models

class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama_jabatan = models.CharField(max_length=100)
    gaji_pokok = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_jabatan


class Karyawan(models.Model):
    id_karyawan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ttl = models.DateField()  # Tanggal lahir
    tgl_bergabung = models.DateField()  # Tanggal bergabung
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    id_jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, related_name='karyawan')

    def __str__(self):
        return self.nama


class Presensi(models.Model):
    id_presensi = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    status = models.CharField(max_length=10, choices=[('hadir', 'Hadir'), ('tidak', 'Tidak'), ('cuti', 'Cuti'), ('sakit', 'Sakit')])
    id_karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE, related_name='presensi')

    def __str__(self):
        return f"Presensi {self.id_karyawan} pada {self.tanggal}"


class Gaji(models.Model):
    id_gaji = models.AutoField(primary_key=True)
    minggu = models.IntegerField()
    bulan = models.IntegerField()
    total_gaji = models.DecimalField(max_digits=15, decimal_places=2)
    id_karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE, related_name='gaji')

    def __str__(self):
        return f"Gaji {self.id_karyawan} - Minggu {self.minggu}, Bulan {self.bulan}"


class Potongan(models.Model):
    id_potongan = models.AutoField(primary_key=True)
    jenis_potongan = models.CharField(max_length=20, choices=[('pinjaman', 'Pinjaman'), ('potongan', 'Potongan')])
    jumlah_potongan = models.DecimalField(max_digits=15, decimal_places=2)
    id_gaji = models.ForeignKey(Gaji, on_delete=models.CASCADE, related_name='potongan')

    def __str__(self):
        return f"Potongan {self.jenis_potongan} sebesar {self.jumlah_potongan}"
