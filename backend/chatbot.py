import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_saran(nama, hasil_carbon, level):
    
    prompt = f"""
    Kamu adalah asisten lingkungan yang ramah dan peduli. 
    Berikan saran personal dalam Bahasa Indonesia.
    
    Data carbon footprint {nama} bulan ini:
    - Listrik: {hasil_carbon['listrik']:.1f} kg CO2
    - Air: {hasil_carbon['air']:.1f} kg CO2
    - Transportasi: {hasil_carbon['transportasi']:.1f} kg CO2
    - Sampah Makanan: {hasil_carbon['sampah']:.1f} kg CO2
    - Total: {hasil_carbon['total']:.1f} kg CO2
    
    Level emisi: {level}
    
    Berikan:
    1. Komentar singkat tentang kondisi mereka
    2. 3 tips spesifik dan actionable untuk mengurangi emisi
    3. Tantangan mingguan yang menyenangkan
    
    Gunakan bahasa yang friendly, semangat, dan tidak menghakimi.
    Gunakan emoji yang relevan.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def chat_lanjutan(nama, hasil_carbon, riwayat_chat):
    
    system_prompt = f"""
    Kamu adalah asisten lingkungan yang ramah bernama EcoBot.
    Kamu sedang membantu {nama} memahami dan mengurangi carbon footprint mereka.
    
    Data carbon footprint mereka:
    - Listrik: {hasil_carbon['listrik']:.1f} kg CO2
    - Air: {hasil_carbon['air']:.1f} kg CO2
    - Transportasi: {hasil_carbon['transportasi']:.1f} kg CO2
    - Sampah Makanan: {hasil_carbon['sampah']:.1f} kg CO2
    - Total: {hasil_carbon['total']:.1f} kg CO2
    
    Jawab pertanyaan mereka dengan ramah, spesifik, dan helpful.
    Selalu dalam Bahasa Indonesia. Gunakan emoji yang relevan.
    """
    
    messages = [{"role": "system", "content": system_prompt}] + riwayat_chat
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=messages
    )
    
    return response.choices[0].message.content