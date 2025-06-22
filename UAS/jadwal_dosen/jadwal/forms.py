# UAS/jadwal_dosen/jadwal/forms.py
from django import forms
from .models import BookingKelas

class BookingKelasForm(forms.ModelForm):
    tanggal = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    waktu_mulai = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    waktu_selesai = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = BookingKelas
        fields = ['matakuliah', 'dosen', 'hari', 'tanggal', 'waktu_mulai', 'waktu_selesai', 'ruangan', 'keterangan']
        labels = {
            'matakuliah': 'Mata Kuliah',
            'dosen': 'Nama Dosen',
            'hari': 'Hari',
            'tanggal': 'Tanggal Booking',
            'waktu_mulai': 'Waktu Mulai',
            'waktu_selesai': 'Waktu Selesai',
            'ruangan': 'Ruangan yang Dibooking',
            'keterangan': 'Keterangan Tambahan',
        }