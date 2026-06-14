-- 1. Distribusi Status Booking
SELECT
    booking_status,
    COUNT(*) AS total_booking
FROM fact_ride_weather
GROUP BY booking_status
ORDER BY total_booking DESC;


-- 2. Kontribusi Pendapatan Berdasarkan Jenis Kendaraan
SELECT
    vehicle_type,
    SUM(booking_value) AS total_revenue,
    ROUND(
        (SUM(booking_value) * 100.0 / SUM(SUM(booking_value)) OVER ())::numeric,
        2
    ) AS revenue_percentage
FROM fact_ride_weather
GROUP BY vehicle_type
ORDER BY total_revenue DESC;


-- 3. Tren Pendapatan Bulanan
SELECT
    month,
    SUM(booking_value) AS total_revenue
FROM fact_ride_weather
GROUP BY month
ORDER BY month;


-- 4. Top 10 Lokasi Pickup
SELECT
    pickup_location,
    COUNT(*) AS total_booking
FROM fact_ride_weather
GROUP BY pickup_location
ORDER BY total_booking DESC
LIMIT 10;


-- 5. Pembatalan Berdasarkan Kondisi Cuaca
SELECT
    weather_condition,
    booking_status,
    COUNT(*) AS total_booking
FROM fact_ride_weather
WHERE booking_status IN (
    'Cancelled by Customer',
    'Cancelled by Driver',
    'No Driver Found'
)
GROUP BY weather_condition, booking_status
ORDER BY weather_condition, total_booking DESC;