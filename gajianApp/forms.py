# casual_karyawan/forms.py
from django import forms
from .models import KaryawanCasual
from .models import Presensi


class KaryawanCasualForm(forms.ModelForm):
    class Meta:
        model = KaryawanCasual
        fields = ['nama', 'email', 'ttl', 'no_hp', 'tgl_bergabung', 'jabatan']
        widgets = {
            'ttl': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Pilih tanggal lahir'}),
            'tgl_bergabung': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Pilih tanggal bergabung'}),
        }
        labels = {
            'ttl': 'Tanggal Lahir',
            'tgl_bergabung': 'Tanggal Bergabung',
        }

    def clean_no_hp(self):
        no_hp = self.cleaned_data.get('no_hp')
        if not no_hp.isdigit():
            raise forms.ValidationError("Nomor HP harus berupa angka.")
        return no_hp

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Password'
        })
    )
    remember_me = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class PresensiForm(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = ['tanggal', 'status', 'karyawan']
        labels = {
            'tanggal': 'Tanggal',
            'status': 'Status Kehadiran',
            'karyawan': 'Nama Karyawan'
        }
        widgets = {
            'tanggal': forms.SelectDateWidget(),
        }