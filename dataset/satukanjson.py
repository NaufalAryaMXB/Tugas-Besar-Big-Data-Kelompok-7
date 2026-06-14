import json
import os
import sys
import glob
import pandas as pd
from datetime import datetime

# Fix encoding untuk Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

SAVE_FOLDER   = r"C:\Users\MSI\Documents\Code\API test\ngambil data cuaca\hasil pull"
OUTPUT_FOLDER = r"C:\Users\MSI\Documents\Code\API test\ngambil data cuaca\hasilcombine"

def gabungkan_semua_json():
    # ── Cari semua file JSON ─────────────────────────────────────────
    pattern = os.path.join(SAVE_FOLDER, "weather_*.json")
    files   = sorted(glob.glob(pattern))

    if not files:
        print("❌ Tidak ada file JSON ditemukan.")
        return

    print(f"Ditemukan {len(files)} file JSON:")
    for f in files:
        print(f"  {os.path.basename(f)}")

    # ── Gabungkan semua data ─────────────────────────────────────────
    all_rows = []

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = json.load(f)

        meta = content.get('metadata', {})
        rows = content.get('data', [])
        all_rows.extend(rows)
        print(f"  ✓ {os.path.basename(filepath)}: "
              f"{len(rows):,} records ({meta.get('month_name', '')})")

    # ── Buat DataFrame ───────────────────────────────────────────────
    df_all              = pd.DataFrame(all_rows)
    df_all['date']      = pd.to_datetime(df_all['date'])
    df_all['month_num'] = df_all['date'].dt.month

    # ── Ringkasan per kota per bulan ─────────────────────────────────
    print(f"\nRingkasan data per kota per bulan (jumlah records):")
    pivot = df_all.groupby(
        ['location', 'month_num']
    ).size().unstack(fill_value=0)
    print(pivot.to_string())

    # ── Cek bulan dan kota yang belum ada ────────────────────────────
    kota_list       = ["Delhi", "Gurgaon", "Noida", "Faridabad",
                       "Ghaziabad", "Sonipat", "Meerut"]
    bulan_list      = list(range(1, 13))
    total_kombinasi = len(kota_list) * len(bulan_list)

    missing = []
    for kota in kota_list:
        for bulan in bulan_list:
            count = len(df_all[
                (df_all['location'] == kota) &
                (df_all['month_num'] == bulan)
            ])
            if count == 0:
                bulan_str = datetime(2024, bulan, 1).strftime('%b %Y')
                missing.append(f"{kota} — {bulan_str}")

    if missing:
        print(f"\n⚠ Data yang belum ada ({len(missing)} dari "
              f"{total_kombinasi} kombinasi):")
        for m in missing:
            print(f"  ✗ {m}")
    else:
        print(f"\n✅ Semua {total_kombinasi} kombinasi "
              f"(7 kota × 12 bulan) sudah lengkap!")

    # ── Sort dan simpan ──────────────────────────────────────────────
    df_all = df_all.sort_values(
        ['location', 'date', 'hour']
    ).reset_index(drop=True)
    df_all = df_all.drop(columns=['month_num'])

    # ── Konversi Timestamp ke string sebelum simpan ──────────────────
    df_for_json          = df_all.copy()
    df_for_json['date']  = df_for_json['date'].dt.strftime('%Y-%m-%d')

    # Konversi semua kolom yang masih Timestamp atau NaT
    for col in df_for_json.columns:
        if df_for_json[col].dtype == 'datetime64[ns]':
            df_for_json[col] = df_for_json[col].dt.strftime('%Y-%m-%d')

    # Konversi NaN ke None agar JSON serializable
    df_for_json = df_for_json.where(pd.notnull(df_for_json), None)

    # Simpan sebagai CSV
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    output_csv = os.path.join(OUTPUT_FOLDER, "weather_ncr_2024_full.csv")
    df_all.to_csv(output_csv, index=False)
    print(f"\n💾 CSV disimpan: {output_csv}")

    # Simpan sebagai JSON
    output_json = os.path.join(OUTPUT_FOLDER, "weather_ncr_2024_full.json")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({
            "metadata": {
                "total_records" : len(df_for_json),
                "cities"        : kota_list,
                "year"          : 2024,
                "columns"       : list(df_for_json.columns),
                "generated_at"  : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            },
            "data": df_for_json.to_dict(orient='records')
        }, f, ensure_ascii=False, indent=2)
    print(f"💾 JSON disimpan: {output_json}")

    print(f"\n{'=' * 55}")
    print(f"✅ Gabungan selesai!")
    print(f"Total records : {len(df_all):,}")
    print(f"Shape         : {df_all.shape}")
    print(f"\nMissing values per kolom:")
    print(df_all.isna().sum().to_string())
    print(f"\nDistribusi kondisi cuaca:")
    print(df_all['conditions'].value_counts().head(10).to_string())

    return df_all

if __name__ == "__main__":
    df = gabungkan_semua_json()