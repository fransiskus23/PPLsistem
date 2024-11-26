from django.apps import AppConfig



class GajianappConfig(AppConfig):  # Ganti 'AppKaryawanConfig' dengan nama kelas aplikasi Anda
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gajianApp'

    def ready(self):
        import gajianApp.signals
