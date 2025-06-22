# UAS/jadwal_dosen/jadwal/models.py
from django.db import models

class BookingKelas(models.Model):
    matakuliah = models.CharField(max_length=100)
    dosen = models.CharField(max_length=100)
    hari = models.CharField(max_length=20)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    ruangan = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.matakuliah} oleh {self.dosen} pada {self.tanggal} di {self.ruangan}"