from fastapi import FastAPI
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Uchrashuv(BaseModel):
    bolim: str
    doktor: str
    ism: str
    email: str
    sana: str
    vaqt: str

@app.post("/uchrashuv/")
def uchrashuv_yaratish(malumot: Uchrashuv):
    with open("uchrashuvlar.txt", "a", encoding="utf-8") as file:
        file.write(json.dumps(malumot.dict()) + "\n")
    return {"message": "Uchrashuv muvaffaqiyatli yaratildi!"}

@app.get("/admin/uchrashuvlar/")
def uchrashuv_olish():
    try:
        with open("uchrashuvlar.txt", "r", encoding="utf-8") as file:
            uchrashuvlar = [json.loads(line) for line in file.readlines()]
        return {"uchrashuvlar": uchrashuvlar}
    except FileNotFoundError:
        return {"uchrashuvlar": []}
