# Generated by Django 5.1 on 2024-09-16 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id_jabatan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_jabatan', models.CharField(max_length=100)),
                ('gaji_pokok', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MasterGaji',
            fields=[
                ('id_master_gaji', models.AutoField(primary_key=True, serialize=False)),
                ('komponen_gaji', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KaryawanCasual',
            fields=[
                ('id_karyawan', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ttl', models.DateField()),
                ('alamat', models.TextField()),
                ('no_hp', models.CharField(max_length=15)),
                ('tgl_bergabung', models.DateField()),
                ('jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gajianApp.jabatan')),
            ],
        ),
        migrations.CreateModel(
            name='Presensi',
            fields=[
                ('id_presensi', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('status', models.CharField(choices=[('hadir', 'Hadir'), ('tidak', 'Tidak Hadir'), ('cuti', 'Cuti'), ('sakit', 'Sakit')], max_length=20)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gajianApp.karyawancasual')),
            ],
        ),
        migrations.CreateModel(
            name='SlipGaji',
            fields=[
                ('id_slip_gaji', models.AutoField(primary_key=True, serialize=False)),
                ('periode', models.CharField(choices=[('minggu', 'Minggu'), ('bulan', 'Bulan'), ('tahun', 'Tahun')], max_length=20)),
                ('total_gaji', models.DecimalField(decimal_places=2, max_digits=12)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gajianApp.karyawancasual')),
            ],
        ),
        migrations.CreateModel(
            name='ItemGaji',
            fields=[
                ('id_item_gaji', models.AutoField(primary_key=True, serialize=False)),
                ('jenis_item', models.CharField(choices=[('gaji_pokok', 'Gaji Pokok'), ('bonus', 'Bonus'), ('pinjaman', 'Pinjaman'), ('potongan', 'Potongan')], max_length=50)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=12)),
                ('slip_gaji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gajianApp.slipgaji')),
            ],
        ),
    ]
