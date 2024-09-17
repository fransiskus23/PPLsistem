from django.db import models

class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama_jabatan = models.CharField(max_length=100)
    gaji_pokok = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_jabatan

class KaryawanCasual(models.Model):
    id_karyawan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ttl = models.DateField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    tgl_bergabung = models.DateField()
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Presensi(models.Model):
    id_presensi = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('hadir', 'Hadir'),
        ('tidak', 'Tidak Hadir'),
        ('cuti', 'Cuti'),
        ('sakit', 'Sakit')
    ])
    karyawan = models.ForeignKey(KaryawanCasual, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.karyawan.nama} - {self.tanggal}"

class MasterGaji(models.Model):
    id_master_gaji = models.AutoField(primary_key=True)
    komponen_gaji = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.komponen_gaji

class SlipGaji(models.Model):
    id_slip_gaji = models.AutoField(primary_key=True)
    karyawan = models.ForeignKey(KaryawanCasual, on_delete=models.CASCADE)
    periode = models.CharField(max_length=20, choices=[
        ('minggu', 'Minggu'),
        ('bulan', 'Bulan'),
        ('tahun', 'Tahun')
    ])
    total_gaji = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Slip Gaji {self.karyawan.nama} - {self.periode}"

class ItemGaji(models.Model):
    id_item_gaji = models.AutoField(primary_key=True)
    slip_gaji = models.ForeignKey(SlipGaji, on_delete=models.CASCADE)
    jenis_item = models.CharField(max_length=50, choices=[
        ('gaji_pokok', 'Gaji Pokok'),
        ('bonus', 'Bonus'),
        ('pinjaman', 'Pinjaman'),
        ('potongan', 'Potongan')
    ])
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.jenis_item} - {self.jumlah}"
