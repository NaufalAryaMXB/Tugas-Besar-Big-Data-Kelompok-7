# Ride Booking & Weather Analytics

## Anggota Kelompok
- Naufal Arya Putra Ultawijaya (1103223204)
- Adhiaris Muhammad Azka (1103220143)


## Deskripsi Project
Project ini bertujuan membandingkan proses ETL dan ELT menggunakan dataset Ride Booking NCR India dan Weather Data NCR India 2024.

## Tools
- Python
- PostgreSQL
- Tableau

## Dataset
### Dataset Ride Booking
https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard

### Dataset Weather
https://www.visualcrossing.com/weather-api

## Struktur Repository

```text
cleaned_data/
dashboard/
database/
dataset/
ETL.ipynb
ELT.ipynb
```

## Dashboard

Dashboard menampilkan:
- Distribusi Status Booking
- Kontribusi Pendapatan Kendaraan
- Tren Pendapatan Bulanan
- Top 10 Lokasi Pickup
- Pengaruh Cuaca terhadap Pembatalan Booking

## Menjalankan Project

### ETL
1. Jalankan ETL.ipynb
2. Hasil tersimpan pada cleaned_data

### ELT
1. Import data ke PostgreSQL
2. Jalankan ELT.ipynb
3. Data dimuat ke tabel fact_ride_weather

### Tableau
1. Hubungkan Tableau ke PostgreSQL
2. Buka file .twb
3. Dashboard siap digunakan