# UAS/jadwal_dosen/jadwal/views.py
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingKelasForm
import os
import io # Pastikan ini ada

# Path ke file Excel Anda.
# os.path.dirname(__file__) -> /UAS/jadwal_dosen/jadwal/
# os.path.dirname(os.path.dirname(__file__)) -> /UAS/jadwal_dosen/
# Maka, EXCEL_FILE akan menunjuk ke /UAS/jadwal_dosen/database_jadwal.xlsx
EXCEL_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database_jadwal.xlsx')

def load_excel_data():
    """Memuat semua data dari semua sheet Excel."""
    data = {}
    try:
        xls = pd.ExcelFile(EXCEL_FILE)
        data['mapping_matakuliah'] = xls.parse('mapping_matakuliah')
        data['jadwal_angkatan_24'] = xls.parse('jadwal_angkatan_24')
        data['jadwal_angkatan_23'] = xls.parse('jadwal_angkatan_23')
        data['jadwal_angkatan_22'] = xls.parse('jadwal_angkatan_22')
        data['pembimbing_akademik'] = xls.parse('pembimbing_akademik')
        # Coba muat sheet bookingan_kelas, jika tidak ada, buat DataFrame kosong
        try:
            data['bookingan_kelas'] = xls.parse('bookingan_kelas')
        except ValueError: # Sheet not found
            data['bookingan_kelas'] = pd.DataFrame(columns=[
                'matakuliah', 'dosen', 'hari', 'tanggal', 'waktu_mulai', 'waktu_selesai', 'ruangan', 'keterangan', 'booked_at'
            ])
    except FileNotFoundError:
        print(f"Error: {EXCEL_FILE} not found. Please create it.")
        # Buat DataFrame kosong jika file tidak ditemukan
        data['mapping_matakuliah'] = pd.DataFrame(columns=['Kode MK', 'Nama MK', 'SKS', 'Dosen Pengampu'])
        data['jadwal_angkatan_24'] = pd.DataFrame(columns=['Hari', 'Waktu Mulai', 'Waktu Selesai', 'Kode MK', 'Kelas', 'Ruang', 'Keterangan'])
        data['jadwal_angkatan_23'] = pd.DataFrame(columns=['Hari', 'Waktu Mulai', 'Waktu Selesai', 'Kode MK', 'Kelas', 'Ruang', 'Keterangan'])
        data['jadwal_angkatan_22'] = pd.DataFrame(columns=['Hari', 'Waktu Mulai', 'Waktu Selesai', 'Kode MK', 'Kelas', 'Ruang', 'Keterangan'])
        data['pembimbing_akademik'] = pd.DataFrame(columns=['NIP Dosen', 'Nama Dosen', 'Angkatan Bimbingan', 'Jumlah Mahasiswa'])
        data['bookingan_kelas'] = pd.DataFrame(columns=[
            'matakuliah', 'dosen', 'hari', 'tanggal', 'waktu_mulai', 'waktu_selesai', 'ruangan', 'keterangan', 'booked_at'
        ])
    return data

def save_excel_data(data):
    """Menyimpan semua data kembali ke Excel."""
    try:
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
            data['mapping_matakuliah'].to_excel(writer, sheet_name='mapping_matakuliah', index=False)
            data['jadwal_angkatan_24'].to_excel(writer, sheet_name='jadwal_angkatan_24', index=False)
            data['jadwal_angkatan_23'].to_excel(writer, sheet_name='jadwal_angkatan_23', index=False)
            data['jadwal_angkatan_22'].to_excel(writer, sheet_name='jadwal_angkatan_22', index=False)
            data['pembimbing_akademik'].to_excel(writer, sheet_name='pembimbing_akademik', index=False)
            data['bookingan_kelas'].to_excel(writer, sheet_name='bookingan_kelas', index=False)
        return True
    except Exception as e:
        print(f"Error saving Excel file: {e}")
        return False

def index(request):
    """Menampilkan semua data jadwal."""
    data = load_excel_data()
    context = {
        # Tambahkan .fillna('') sebelum .to_html() untuk setiap DataFrame
        'mapping_matakuliah': data['mapping_matakuliah'].fillna('').to_html(classes='table table-striped table-bordered'),
        'jadwal_angkatan_24': data['jadwal_angkatan_24'].fillna('').to_html(classes='table table-striped table-bordered'),
        'jadwal_angkatan_23': data['jadwal_angkatan_23'].fillna('').to_html(classes='table table-striped table-bordered'),
        'jadwal_angkatan_22': data['jadwal_angkatan_22'].fillna('').to_html(classes='table table-striped table-bordered'),
        'pembimbing_akademik': data['pembimbing_akademik'].fillna('').to_html(classes='table table-striped table-bordered'),
        'bookingan_kelas': data['bookingan_kelas'].fillna('').to_html(classes='table table-striped table-bordered'),
    }
    return render(request, 'jadwal/index.html', context)

def booking_kelas(request):
    """Fitur booking kelas."""
    if request.method == 'POST':
        form = BookingKelasForm(request.POST)
        if form.is_valid():
            booking_data = form.cleaned_data
            
            # Format time correctly for Excel
            booking_data['waktu_mulai'] = booking_data['waktu_mulai'].strftime('%H:%M')
            booking_data['waktu_selesai'] = booking_data['waktu_selesai'].strftime('%H:%M')
            booking_data['tanggal'] = booking_data['tanggal'].strftime('%Y-%m-%d')
            booking_data['booked_at'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')

            all_data = load_excel_data()
            bookingan_df = all_data['bookingan_kelas']

            new_booking_df = pd.DataFrame([booking_data])
            bookingan_df = pd.concat([bookingan_df, new_booking_df], ignore_index=True)
            
            all_data['bookingan_kelas'] = bookingan_df

            if save_excel_data(all_data):
                return redirect('booking_success')
            else:
                return render(request, 'jadwal/booking_form.html', {'form': form, 'error_message': 'Gagal menyimpan booking. Silakan coba lagi.'})
    else:
        form = BookingKelasForm()
    return render(request, 'jadwal/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'jadwal/success.html')

def export_excel(request):
    """Export semua data jadwal ke file Excel."""
    data = load_excel_data()
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        data['mapping_matakuliah'].to_excel(writer, sheet_name='mapping_matakuliah', index=False)
        data['jadwal_angkatan_24'].to_excel(writer, sheet_name='jadwal_angkatan_24', index=False)
        data['jadwal_angkatan_23'].to_excel(writer, sheet_name='jadwal_angkatan_23', index=False)
        data['jadwal_angkatan_22'].to_excel(writer, sheet_name='jadwal_angkatan_22', index=False)
        data['pembimbing_akademik'].to_excel(writer, sheet_name='pembimbing_akademik', index=False)
        data['bookingan_kelas'].to_excel(writer, sheet_name='bookingan_kelas', index=False)
    
    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="jadwal_dosen_terbaru.xlsx"'
    return response