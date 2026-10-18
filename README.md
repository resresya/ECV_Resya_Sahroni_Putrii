# E-CV Resya Sahroni Putri — Peach Pink (Google Drive Links)

## Cara menambahkan tautan Google Drive

Buka `app.py` dan isi URL pada bagian konfigurasi di awal file.

### 1. Link bukti IPK kumulatif
Cari `PROFILE`, lalu isi `ipk_url`:
```python
"ipk_url": "https://drive.google.com/file/d/ID_FILE/view",
```
Tombol **Lihat Bukti IPK** akan muncul di bawah kartu IPK jika URL sudah diisi.

### 2. Link KHS per semester
Isi kolom `url` pada `SEMESTERS`:
```python
{"name": "Semester 1", "ip": "4,00", "url": "https://drive.google.com/file/d/ID_FILE/view"},
```
Lakukan hal yang sama untuk Semester 2, 3, dan 4. Tombol **Lihat KHS** akan muncul pada semester yang memiliki URL.

### 3. Link sertifikat
Pada `CERTIFICATES`, isi kolom ketiga setiap sertifikat:
```python
("Database Administrator – BNSP", "Sertifikasi Kompetensi", "https://drive.google.com/file/d/ID_FILE/view"),
```
Tombol **Lihat ↗** akan muncul pada setiap sertifikat yang memiliki URL.

## Pengaturan Google Drive
Pada setiap file/folder, pilih **Bagikan** lalu ubah akses menjadi **Siapa saja yang memiliki link — Pelihat**. Salin link dan tempel ke `app.py`.

## Upload
Unggah `app.py`, `requirements.txt`, dan `README.md` ke repository GitHub. Timpa `app.py` yang lama, lalu commit perubahan. Jika repository sudah terhubung ke Streamlit Cloud, aplikasi akan diperbarui otomatis.

Untuk tombol unduh PDF, letakkan `CV_Resya_Sahroni_Putri.pdf` di folder yang sama dengan `app.py`. Foto profil opsional: `profile.jpg`.
