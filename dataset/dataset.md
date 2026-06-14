# Dokumentasi Dataset

## Dataset 1: NCR Uber Ride Bookings 2024

| Informasi | Detail |
|------------|---------|
| Nama Dataset | NCR Uber Ride Bookings 2024 |
| Sumber | Kaggle |
| Link | https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard |
| File Utama | ncr_ride_bookings.csv |
| Deskripsi | Dataset berisi data pemesanan layanan ride-hailing di wilayah NCR (National Capital Region) India selama tahun 2024. Dataset mencakup informasi booking, pelanggan, kendaraan, lokasi pickup dan drop, status perjalanan, metode pembayaran, serta nilai transaksi. |
| Digunakan Untuk | Analisis status booking, performa kendaraan, tren pendapatan, dan lokasi pickup. |

---

## Dataset 2: NCR Weather Data 2024

| Informasi | Detail |
|------------|---------|
| Nama Dataset | NCR Weather Data 2024 |
| Sumber | Visual Crossing Weather API |
| Link | https://www.visualcrossing.com/weather-api |
| Format Data | JSON  |
| Deskripsi | Dataset cuaca historis untuk wilayah NCR India selama tahun 2024 yang berisi suhu, kelembaban, curah hujan, kecepatan angin, visibilitas, dan kondisi cuaca per jam. |
| Digunakan Untuk | Analisis hubungan kondisi cuaca terhadap aktivitas ride booking dan pembatalan perjalanan. |

---

# Proses Pengambilan Data Cuaca

Data cuaca diperoleh menggunakan Visual Crossing Weather API melalui script Python `ambildata.py`.

Proses yang dilakukan:

1. Menentukan kota target dan bulan yang akan diambil.
2. Mengirim request ke Visual Crossing Weather API.
3. Mengambil data cuaca historis per jam.
4. Melakukan decoding kondisi cuaca agar lebih mudah dibaca.
5. Menyimpan hasil ke dalam file JSON.

Kota yang digunakan:

- Delhi
- Gurgaon
- Noida
- Faridabad
- Ghaziabad
- Sonipat
- Meerut

Atribut cuaca yang diambil meliputi:

- Temperature
- Feels Like
- Humidity
- Rainfall
- Visibility
- Wind Speed
- Cloud Cover
- UV Index
- Weather Condition

File script:

```text
ambildata.py
```

---

# Proses Penggabungan Data Cuaca

Setelah seluruh data cuaca berhasil diperoleh dari API, dilakukan proses penggabungan seluruh file JSON menggunakan script Python `satukanjson.py`.

Proses yang dilakukan:

1. Membaca seluruh file JSON hasil pengambilan data cuaca.
2. Menggabungkan seluruh data menjadi satu DataFrame.
3. Memvalidasi kelengkapan data untuk seluruh kota dan bulan.
4. Melakukan sorting data berdasarkan lokasi, tanggal, dan jam.
5. Menyimpan hasil gabungan menjadi satu file CSV dan JSON.

Output yang dihasilkan:

```text
weather_ncr_2024_full.csv
weather_ncr_2024_full.json
```

File script:

```text
satukanjson.py
```

---
