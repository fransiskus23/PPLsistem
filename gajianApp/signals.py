from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import KaryawanCasual

@receiver(post_save, sender=KaryawanCasual)
def sync_karyawan_to_user(sender, instance, created, **kwargs):
    if created:
        # Sinkronisasi data karyawan ke auth_user dengan password default
        instance.create_auth_user(password="defaultpassword123")  # Ganti password default jika perlu
