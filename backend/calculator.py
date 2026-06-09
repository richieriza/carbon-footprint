# Emission factors (kg CO2 per unit)
EMISSION_FACTORS = {
    "listrik": 0.87,      # kg CO2 per kWh (Indonesia)
    "air": 0.001,         # kg CO2 per liter
    "transportasi": 0.21, # kg CO2 per km (motor/mobil rata-rata)
    "sampah": 2.5,        # kg CO2 per kg sampah makanan
}

# Rata-rata emisi rumah tangga Indonesia per bulan (kg CO2)
RATA_RATA_INDONESIA = {
    "listrik": 87,
    "air": 3,
    "transportasi": 63,
    "sampah": 12.5,
    "total": 165.5
}

def hitung_carbon(listrik_kwh, air_liter, transportasi_km, sampah_kg):
    hasil = {
        "listrik": listrik_kwh * EMISSION_FACTORS["listrik"],
        "air": air_liter * EMISSION_FACTORS["air"],
        "transportasi": transportasi_km * EMISSION_FACTORS["transportasi"],
        "sampah": sampah_kg * EMISSION_FACTORS["sampah"],
    }
    hasil["total"] = sum(hasil.values())
    return hasil

def konversi_metafora(total_co2):
    return {
        "pohon": round(total_co2 / 21, 2),        # 1 pohon serap 21 kg CO2/bulan
        "rupiah": round(total_co2 * 500),          # estimasi biaya karbon
    }

def cek_level(total_co2):
    if total_co2 < 100:
        return "rendah"
    elif total_co2 < 200:
        return "sedang"
    else:
        return "tinggi"