from django.core.management.base import BaseCommand
from gajianApp.models import KaryawanCasual  # Ganti sesuai nama aplikasi dan model Anda
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Sinkronisasi data karyawan ke tabel auth_user'

    def handle(self, *args, **kwargs):
        karyawan_list = KaryawanCasual.objects.all()
        for karyawan in karyawan_list:
            # Buat atau dapatkan pengguna dari tabel auth_user
            user, created = User.objects.get_or_create(username=karyawan.nama, email=karyawan.email)
            if created:
                # Set password default untuk pengguna baru
                user.set_password('default123')  # Password default
                user.save()
        self.stdout.write(self.style.SUCCESS('Berhasil menyinkronkan data karyawan ke auth_user.'))