# Struktur Tabel Dataset

## 1. `ride_bookings_weather_merged.` (ETL)

Hasil gabungan data pemesanan perjalanan NCR dengan data cuaca.

| No  | Nama Kolom                        | Tipe Data | Keterangan                                       |
| --- | --------------------------------- | --------- | ------------------------------------------------ |
| 1   | Date                              | string    | Tanggal pemesanan (YYYY-MM-DD)                   |
| 2   | Time                              | string    | Waktu pemesanan (HH:MM:SS)                       |
| 3   | Booking ID                        | string    | ID unik pemesanan                                |
| 4   | Booking Status                    | string    | Status pemesanan (Success, Cancelled, dll.)      |
| 5   | Customer ID                       | string    | ID unik pelanggan                                |
| 6   | Vehicle Type                      | string    | Jenis kendaraan yang dipesan                     |
| 7   | Pickup Location                   | string    | Lokasi penjemputan                               |
| 8   | Drop Location                     | string    | Lokasi tujuan                                    |
| 9   | Avg VTAT                          | float     | Rata-rata waktu kedatangan kendaraan (menit)     |
| 10  | Avg CTAT                          | float     | Rata-rata waktu konfirmasi pelanggan (menit)     |
| 11  | Cancelled Rides by Customer       | integer   | Jumlah pembatalan oleh pelanggan                 |
| 12  | Reason for cancelling by Customer | float     | Alasan pembatalan oleh pelanggan                 |
| 13  | Cancelled Rides by Driver         | integer   | Jumlah pembatalan oleh driver                    |
| 14  | Driver Cancellation Reason        | float     | Alasan pembatalan oleh driver                    |
| 15  | Incomplete Rides                  | integer   | Jumlah perjalanan tidak selesai                  |
| 16  | Incomplete Rides Reason           | string    | Alasan perjalanan tidak selesai                  |
| 17  | Booking Value                     | float     | Nilai transaksi pemesanan (mata uang lokal)      |
| 18  | Ride Distance                     | float     | Jarak perjalanan (km)                            |
| 19  | Driver Ratings                    | float     | Rating pelanggan terhadap driver (1–5)           |
| 20  | Customer Rating                   | float     | Rating driver terhadap pelanggan (1–5)           |
| 21  | Payment Method                    | string    | Metode pembayaran yang digunakan                 |
| 22  | Booking Datetime                  | string    | Gabungan tanggal dan waktu pemesanan             |
| 23  | Hour                              | integer   | Jam pemesanan (0–23)                             |
| 24  | Month                             | integer   | Bulan pemesanan (1–12)                           |
| 25  | Month Name                        | string    | Nama bulan pemesanan                             |
| 26  | Pickup City                       | string    | Kota penjemputan                                 |
| 27  | Drop City                         | string    | Kota tujuan                                      |
| 28  | temperature_c                     | float     | Suhu udara saat pemesanan (°C)                   |
| 29  | feelslike_c                       | float     | Suhu terasa saat pemesanan (°C)                  |
| 30  | humidity_pct                      | float     | Kelembaban udara (%)                             |
| 31  | visibility_km                     | float     | Jarak pandang (km)                               |
| 32  | rainfall_mm                       | float     | Curah hujan (mm)                                 |
| 33  | windspeed_kmh                     | float     | Kecepatan angin (km/h)                           |
| 34  | conditions                        | string    | Kondisi cuaca singkat (Clear, Rain, dll.)        |
| 35  | description                       | string    | Deskripsi cuaca lebih detail                     |
| 36  | icon                              | string    | Kode ikon cuaca                                  |
| 37  | Temperature Category              | string    | Kategori suhu (Cold, Warm, Hot, dll.)            |
| 38  | Rain Category                     | string    | Kategori hujan (Tidak Hujan, Hujan Ringan, dll.) |
| 39  | Visibility Category               | string    | Kategori jarak pandang (Rendah, Sedang, Tinggi)  |

---

## 2. `fact_ride_weather` (ELT)

Tabel fakta hasil transformasi ELT, siap digunakan untuk analisis dan pelaporan.

| No  | Nama Kolom        | Tipe Data | Keterangan                                   |
| --- | ----------------- | --------- | -------------------------------------------- |
| 1   | booking_id        | string    | ID unik pemesanan                            |
| 2   | customer_id       | string    | ID unik pelanggan                            |
| 3   | ride_date         | string    | Tanggal perjalanan (YYYY-MM-DD)              |
| 4   | hour              | integer   | Jam pemesanan (0–23)                         |
| 5   | month             | integer   | Bulan pemesanan (1–12)                       |
| 6   | booking_status    | string    | Status pemesanan                             |
| 7   | vehicle_type      | string    | Jenis kendaraan                              |
| 8   | pickup_location   | string    | Lokasi penjemputan                           |
| 9   | drop_location     | string    | Lokasi tujuan                                |
| 10  | booking_value     | float     | Nilai transaksi pemesanan                    |
| 11  | ride_distance     | float     | Jarak perjalanan (km)                        |
| 12  | driver_rating     | float     | Rating driver (1–5)                          |
| 13  | customer_rating   | float     | Rating pelanggan (1–5)                       |
| 14  | payment_method    | string    | Metode pembayaran                            |
| 15  | avg_vtat          | float     | Rata-rata waktu kedatangan kendaraan (menit) |
| 16  | avg_ctat          | float     | Rata-rata waktu konfirmasi pelanggan (menit) |
| 17  | city              | string    | Kota lokasi perjalanan                       |
| 18  | temperature_c     | float     | Suhu udara (°C)                              |
| 19  | humidity_pct      | float     | Kelembaban udara (%)                         |
| 20  | rainfall_mm       | float     | Curah hujan (mm)                             |
| 21  | windspeed_kmh     | float     | Kecepatan angin (km/h)                       |
| 22  | visibility_km     | float     | Jarak pandang (km)                           |
| 23  | weather_condition | string    | Kondisi cuaca (Clear, Rain, dll.)            |
| 24  | is_rainy          | integer   | Flag hujan: 1 = hujan, 0 = tidak hujan       |
| 25  | temp_category     | string    | Kategori suhu (Cold, Warm, Hot, dll.)        |
