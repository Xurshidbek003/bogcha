import os
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud
import database
import models
import schemas
from database import engine
from dotenv import load_dotenv
from google import genai
from google.genai import types


try:
    load_dotenv()
except ImportError:
    pass

# Yangi unifikatsiyalangan Google GenAI SDK (google-genai).
# Eski "google-generativeai" SDK eskirgan, shuning uchun ishlatilmaydi.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai_client = None
if GOOGLE_API_KEY:
    try:
        genai_client = genai.Client(api_key=GOOGLE_API_KEY)
    except ImportError:
        genai_client = None

SYSTEM_PROMPT = (
    "Sen 'KinderBot' — bog'cha qidirish saytining samimiy va aqlli yordamchisisan. "
    "Foydalanuvchining savoliga FAQAT senga berilgan MA'LUMOTLAR asosida, o'zbek tilida, "
    "qisqa va aniq javob ber. Agar so'ralgan ma'lumot ro'yxatda bo'lmasa, buni ochiq ayt "
    "va mavjud bog'chalardan mosini tavsiya qil. Hech qachon ma'lumot to'qib chiqarma."
)


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Kindergarten CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



class ChatRequest(BaseModel):
    message: str


def build_kindergarten_context(db: Session) -> str:
    kindergartens = db.query(models.Kindergarten).all()
    if not kindergartens:
        return "Hozircha bazada bog'chalar yo'q."

    lines = ["Bizda mavjud bog'chalar:"]
    for k in kindergartens:
        langs = ", ".join(k.languages or []) or "—"
        progs = ", ".join(k.programs or []) or "—"
        lines.append(
            f"- ID: {k.id}, Nomi: {k.name}, Manzil: {k.region} {k.district}, "
            f"Narxi: {k.price}, Reyting: {k.rating}, Tillar: {langs}, Dasturlar: {progs}."
        )
    return "\n".join(lines)


@app.post("/api/chat")
def chat_bot(request: ChatRequest, db: Session = Depends(database.get_db)):
    user_message = (request.message or "").strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Savol bo'sh bo'lishi mumkin emas.")

    if genai_client is None:
        raise HTTPException(
            status_code=503,
            detail="AI xizmati sozlanmagan. GOOGLE_API_KEY ni .env faylga qo'shing.",
        )

    data_text = build_kindergarten_context(db)
    prompt = f"MA'LUMOTLAR:\n{data_text}\n\nFOYDALANUVCHI SAVOLI:\n{user_message}"

    try:
        response = genai_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
            ),
        )
        ai_reply = (response.text or "").replace("*", "").strip()
        if not ai_reply:
            ai_reply = "Uzr, savolga javob topa olmadim. Boshqacharoq so'rab ko'ring."
    except Exception as e:  # noqa: BLE001
        print(f"AI Xatoligi: {e}")
        ai_reply = "Uzr, hozir tizimda vaqtinchalik nosozlik bor. Keyinroq urinib ko'ring."

    return {"response": ai_reply}



@app.get("/admin")
async def read_admin():
    return FileResponse("static/index.html")



@app.post(
    "/api/kindergartens",
    response_model=schemas.Kindergarten,
    status_code=status.HTTP_201_CREATED,
)
def create_kindergarten(item: schemas.KindergartenCreate, db: Session = Depends(database.get_db)):
    return crud.create_kindergarten(db=db, item=item)


@app.get("/api/kindergartens", response_model=List[schemas.Kindergarten])
def read_kindergartens(
    region: Optional[str] = None,
    type: Optional[str] = None,
    db: Session = Depends(database.get_db),
):
    return crud.get_kindergartens(db, region=region, type=type)


@app.get("/api/kindergartens/{kg_id}", response_model=schemas.Kindergarten)
def read_kindergarten(kg_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_kindergarten(db, kg_id=kg_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Bog'cha topilmadi")
    return db_item


@app.put("/api/kindergartens/{kg_id}", response_model=schemas.Kindergarten)
def update_kindergarten(
    kg_id: int, item: schemas.KindergartenUpdate, db: Session = Depends(database.get_db)
):
    db_item = crud.update_kindergarten(db, kg_id=kg_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Bog'cha topilmadi")
    return db_item


@app.delete("/api/kindergartens/{kg_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kindergarten(kg_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_kindergarten(db, kg_id=kg_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bog'cha topilmadi")
    return None


@app.post("/api/kindergartens/{kg_id}/reviews", response_model=schemas.Review)
def create_review_for_kindergarten(
    kg_id: int, review: schemas.ReviewCreate, db: Session = Depends(database.get_db)
):
    return crud.create_review(db=db, kg_id=kg_id, review=review)


app.mount("/admin", StaticFiles(directory="static", html=True), name="static")