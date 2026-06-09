from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from backend.calculator import hitung_carbon, konversi_metafora, cek_level
from backend.chatbot import get_saran, chat_lanjutan
from fastapi.responses import FileResponse

app = FastAPI()

# Izinkan frontend akses backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Model data input
class InputCarbon(BaseModel):
    nama: str
    listrik_kwh: float
    air_liter: float
    transportasi_km: float
    sampah_kg: float

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    nama: str
    hasil_carbon: dict
    riwayat_chat: List[ChatMessage]

# Route hitung carbon
@app.post("/hitung")
def hitung(data: InputCarbon):
    hasil = hitung_carbon(
        data.listrik_kwh,
        data.air_liter,
        data.transportasi_km,
        data.sampah_kg
    )
    metafora = konversi_metafora(hasil["total"])
    level = cek_level(hasil["total"])
    saran = ""

    if level == "tinggi":
        saran = get_saran(data.nama, hasil, level)

    return {
        "nama": data.nama,
        "hasil": hasil,
        "metafora": metafora,
        "level": level,
        "saran": saran
    }

# Route chat lanjutan
@app.post("/chat")
def chat(data: ChatRequest):
    riwayat = [{"role": m.role, "content": m.content} 
               for m in data.riwayat_chat]
    balasan = chat_lanjutan(data.nama, data.hasil_carbon, riwayat)
    return {"balasan": balasan}

# Route cek server
@app.get("/")
def root():
    return FileResponse("frontend/index.html")