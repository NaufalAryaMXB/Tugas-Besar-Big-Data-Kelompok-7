# Ride Booking & Weather Analytics

## Anggota Kelompok
- Naufal Arya Putra Ultawijaya (1103223204)
- Adhiaris Muhammad Azka (1103220143)

## Deskripsi Project
Project ini bertujuan membandingkan proses ETL dan ELT menggunakan dataset Ride Booking NCR India dan Weather Data NCR India 2024. Data hasil proses diunggah dan disimpan pada database cloud Supabase PostgreSQL untuk keperluan analisis lanjutan.

## Tools
- **Bahasa Pemrograman**: Python
- **Database Cloud**: Supabase (PostgreSQL)
- **Visualisasi Data**: Tableau Desktop
- **Jaringan**: Cloudflare WARP (hanya dibutuhkan jika menggunakan WiFi Kampus/jaringan yang memblokir port database)

## Dataset
### Dataset Ride Booking
https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard

### Dataset Weather
https://www.visualcrossing.com/weather-api

## Struktur Repository
```text
cleaned_data/   -> Folder berisi hasil dataset bersih proses ETL (.csv)
dashboard/      -> Folder berisi file visualisasi Tableau (.twb)
database/       -> Folder berisi dokumentasi skema tabel dan query analitik
dataset/        -> Folder berisi dataset mentah (CSV dan JSON) dan script API
ETL.ipynb       -> Notebook proses ETL (Extract-Transform-Load)
ELT.ipynb       -> Notebook proses ELT (Extract-Load-Transform)
```

## Dashboard Analitik (Tableau)
Dashboard menampilkan visualisasi dari database:
- Distribusi Status Booking
- Kontribusi Pendapatan Kendaraan
- Tren Pendapatan Bulanan
- Top 10 Lokasi Pickup
- Pengaruh Cuaca terhadap Pembatalan Booking

---

## Panduan Menjalankan Project

> [!IMPORTANT]
> **Prasyarat Jaringan (Koneksi Supabase)**:
> - **Koneksi Normal (Seluler/WiFi Rumah)**: Anda bisa langsung menjalankan notebook dan menghubungkan Tableau secara langsung (**Direct**) tanpa perlu menyalakan VPN/WARP.
> - **Koneksi WiFi Kampus**: Anda **wajib mengaktifkan Cloudflare WARP** (atau VPN) terlebih dahulu sebelum menjalankan notebook atau membuka Tableau agar koneksi ke database tidak terblokir oleh firewall kampus.

### 1. Proses ETL
1. Buka notebook [ETL.ipynb](ETL.ipynb).
2. Pada **Cell 11** (Langkah 5), sesuaikan konfigurasi koneksi database Supabase Anda (Host, User, Password, Port: 5432, DB Name: postgres).
3. Jalankan seluruh sel di notebook.
4. Hasil pembersihan lokal akan disimpan di folder `cleaned_data/` dan data hasil gabungan (*merged*) diunggah ke tabel `ride_bookings_weather_merged` di Supabase.

### 2. Proses ELT
1. Buka notebook [ELT.ipynb](ELT.ipynb).
2. Pada **Cell 3**, sesuaikan koneksi string SQLAlchemy (`PG_CONN`) menggunakan URI Supabase Anda (pastikan menyertakan parameter `?sslmode=require`).
3. Jalankan seluruh sel di notebook secara berurutan.
4. Data mentah akan diunggah ke database, dibersihkan, dan diproses langsung di server Supabase menjadi tabel fakta `fact_ride_weather`.

### 3. Visualisasi Tableau
1. Hubungkan Tableau Desktop ke database menggunakan konektor **PostgreSQL**.
2. Masukkan info server Supabase Anda, centang opsi **Require SSL**, dan klik **Sign In**.
3. Di panel Schema, pilih **`public`** dan pilih tabel `fact_ride_weather` atau `ride_bookings_weather_merged` untuk visualisasi.
4. Buka file `.twb` di folder `dashboard/` untuk menggunakan dashboard analitik yang sudah dibuat.