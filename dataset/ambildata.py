import requests
import json
import time
import os
from datetime import datetime, timedelta

# ── GANTI TIGA VARIABEL INI SETIAP JALANKAN ─────────────────────────
API_KEY      = "ISI_API_KEY_DISINI"
TARGET_MONTH = 2          # 2=Feb, 3=Mar, ..., 12=Des
TARGET_CITY  = "Ghaziabad"  # Ghaziabad / Sonipat / Meerut

# ── Konfigurasi ──────────────────────────────────────────────────────
SAVE_FOLDER = r"lokasi save file cuaca"

CITY_MAP = {
    "Delhi"    : "Delhi,India",
    "Gurgaon"  : "Gurugram,Haryana,India",
    "Noida"    : "Noida,Uttar Pradesh,India",
    "Faridabad": "Faridabad,Haryana,India",
    "Ghaziabad": "Ghaziabad,Uttar Pradesh,India",
    "Sonipat"  : "Sonipat,Haryana,India",
    "Meerut"   : "Meerut,Uttar Pradesh,India",
}

CONDITIONS_MAP = {
    "type_1" : "Snow", "type_2" : "Snow Showers",
    "type_3" : "Freezing Drizzle", "type_4" : "Sleet",
    "type_5" : "Rain And Snow", "type_6" : "Freezing Rain",
    "type_7" : "Drizzle", "type_8" : "Heavy Rain",
    "type_9" : "Rain", "type_10": "Heavy Drizzle",
    "type_11": "Light Drizzle", "type_12": "Light Rain",
    "type_13": "Heavy Rain And Snow", "type_14": "Light Rain And Snow",
    "type_15": "Light Snow", "type_16": "Heavy Snow",
    "type_17": "Light Sleet", "type_18": "Thunderstorm",
    "type_19": "Tropical Storm", "type_20": "Hurricane",
    "type_21": "Stormy", "type_22": "Windy",
    "type_23": "Foggy", "type_24": "Haze",
    "type_25": "Smoke", "type_26": "Dust",
    "type_27": "Tornado", "type_28": "Ice",
    "type_29": "Overcast", "type_41": "Overcast",
    "type_42": "Partly Cloudy", "type_43": "Clear",
}

def decode_conditions(raw):
    if not raw:
        return None
    parts   = [p.strip() for p in str(raw).split(',')]
    decoded = [CONDITIONS_MAP.get(p, p) for p in parts]
    return ', '.join(decoded)

def fetch_hourly(location_query, year, month, api_key):
    start  = datetime(year, month, 1)
    end    = (datetime(year, month + 1, 1) - timedelta(days=1)
              if month < 12 else datetime(year, 12, 31))
    url    = (f"https://weather.visualcrossing.com/VisualCrossingWebServices"
              f"/rest/services/timeline/{location_query}"
              f"/{start.strftime('%Y-%m-%d')}/{end.strftime('%Y-%m-%d')}")
    params = {
        "unitGroup"  : "metric",
        "include"    : "hours",
        "key"        : api_key,
        "contentType": "json",
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 429:
            print(f"  ⚠ Kuota habis untuk akun ini.")
            return "QUOTA_EXCEEDED"
        elif r.status_code == 401:
            print(f"  ⚠ API key tidak valid.")
            return "INVALID_KEY"
        else:
            print(f"  Error {r.status_code}: {r.text[:150]}")
            return None
    except Exception as e:
        print(f"  Request error: {e}")
        return None

def parse_hourly(data, location_name):
    rows = []
    if not data or 'days' not in data:
        return rows
    for day in data['days']:
        for hour in day.get('hours', []):
            raw_cond = hour.get('conditions', '')
            rows.append({
                'date'           : day.get('datetime'),
                'time'           : hour.get('datetime'),
                'hour'           : int(hour.get('datetime',
                                       '00:00:00').split(':')[0]),
                'location'       : location_name,
                'temperature_c'  : hour.get('temp'),
                'feelslike_c'    : hour.get('feelslike'),
                'dew_point_c'    : hour.get('dew'),
                'humidity_pct'   : hour.get('humidity'),
                'pressure_hpa'   : hour.get('pressure'),
                'visibility_km'  : hour.get('visibility'),
                'cloudcover_pct' : hour.get('cloudcover'),
                'uvindex'        : hour.get('uvindex'),
                'rainfall_mm'    : hour.get('precip', 0.0),
                'precip_prob_pct': hour.get('precipprob'),
                'precip_type'    : hour.get('preciptype'),
                'windspeed_kmh'  : hour.get('windspeed'),
                'winddir_deg'    : hour.get('winddir'),
                'windgust_kmh'   : hour.get('windgust'),
                'conditions_raw' : raw_cond,
                'conditions'     : decode_conditions(raw_cond),
                'description'    : day.get('description'),
                'icon'           : hour.get('icon'),
            })
    return rows

def main():
    # ── Validasi kota ────────────────────────────────────────────────
    if TARGET_CITY not in CITY_MAP:
        print(f"❌ Kota '{TARGET_CITY}' tidak valid.")
        print(f"   Pilihan: {list(CITY_MAP.keys())}")
        return

    # ── Validasi kota yang masih perlu diambil ───────────────────────
    kota_selesai = ["Delhi", "Gurgaon", "Noida", "Faridabad"]
    if TARGET_CITY in kota_selesai:
        print(f"⚠ {TARGET_CITY} sudah lengkap 12/12, tidak perlu diambil lagi.")
        return