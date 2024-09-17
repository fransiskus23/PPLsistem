# casual_karyawan/forms.py
from django import forms
from .models import KaryawanCasual

class KaryawanCasualForm(forms.ModelForm):
    class Meta:
        model = KaryawanCasual
        fields = ['nama', 'email', 'ttl', 'no_hp', 'tgl_bergabung', 'jabatan']
