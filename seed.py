"""
seed.py — bazaga namuna bog'chalar qo'shish uchun skript.

Ishga tushirish:
    python seed.py            # mavjud bo'lmaganlarini qo'shadi (xavfsiz: takror ishlatsa dublikat yaratmaydi)
    python seed.py --reset    # avval BARCHA bog'chalarni o'chirib, qaytadan to'ldiradi

Eslatma: image va gallery'dagi rasmlar — vaqtinchalik (placeholder) rasmlar.
Keyinchalik admin panel orqali ularni o'z rasmlaringizga almashtirishingiz mumkin.
"""

import sys

import models
from database import SessionLocal, engine

# Jadvallar mavjud bo'lmasa — yaratamiz
models.Base.metadata.create_all(bind=engine)


def img(seed: str) -> str:
    """Placeholder rasm URL (picsum.photos har bir 'seed' uchun barqaror rasm beradi)."""
    return f"https://picsum.photos/seed/{seed}/800/500"


# Standart ish vaqti shablonlari
HOURS_FULL = [
    {"day": "Dushanba - Juma", "time": "08:00 - 18:00"},
    {"day": "Shanba", "time": "09:00 - 13:00"},
    {"day": "Yakshanba", "time": "Dam olish"},
]
HOURS_WEEKDAY = [
    {"day": "Dushanba - Juma", "time": "07:30 - 19:00"},
    {"day": "Shanba - Yakshanba", "time": "Dam olish"},
]


KINDERGARTENS = [
    {
        "name": "Gulxan",
        "region": "Toshkent",
        "district": "Chilonzor",
        "type": "davlat",
        "programs": ["Maktabga tayyorlov", "Rasm chizish", "Musiqa"],
        "languages": ["o'zbek", "rus"],
        "price": 450000,
        "rating": 4.3,
        "image": img("gulxan"),
        "short_description": "Chilonzordagi tajribali davlat bog'chasi, qulay narx.",
        "location_address": "Toshkent sh., Chilonzor tumani, Bunyodkor ko'chasi 12",
        "phone": "+998 71 277 14 22",
        "ages": "3-7 yosh",
        "capacity": 180,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat (3 mahal)", "Tibbiy xizmat", "O'yin maydonchasi", "CCTV kuzatuv"],
        "gallery": [img("gulxan-1"), img("gulxan-2"), img("gulxan-3")],
        "full_description": (
            "Gulxan bolalar bog'chasi 1995-yildan beri faoliyat yuritadi. "
            "Tajribali tarbiyachilar, sog'lom ovqatlanish va maktabga puxta tayyorgarlik dasturi mavjud."
        ),
    },
    {
        "name": "Little Genius",
        "region": "Toshkent",
        "district": "Mirzo Ulug'bek",
        "type": "montessori",
        "programs": ["Montessori", "Ingliz tili", "Mental arifmetika", "Robototexnika"],
        "languages": ["o'zbek", "ingliz"],
        "price": 2200000,
        "rating": 4.9,
        "image": img("littlegenius"),
        "short_description": "Zamonaviy Montessori metodikasi va ingliz tili.",
        "location_address": "Toshkent sh., Mirzo Ulug'bek tumani, Buyuk Ipak Yo'li 145",
        "phone": "+998 90 311 88 90",
        "ages": "2-6 yosh",
        "capacity": 60,
        "hours": HOURS_FULL,
        "features": ["Bassein", "Ingliz tilida muloqot", "STEM xona", "Konditsioner", "Transport", "Tibbiy xizmat"],
        "gallery": [img("littlegenius-1"), img("littlegenius-2"), img("littlegenius-3")],
        "full_description": (
            "Little Genius — xalqaro Montessori standartlari asosida ishlaydigan premium bog'cha. "
            "Kichik guruhlar, individual yondashuv va kun davomida ingliz tilida muhit."
        ),
    },
    {
        "name": "Quyoshcha",
        "region": "Samarqand",
        "district": "Samarqand shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Ingliz tili", "Sport", "Rasm chizish"],
        "languages": ["o'zbek", "rus", "ingliz"],
        "price": 1100000,
        "rating": 4.6,
        "image": img("quyoshcha"),
        "short_description": "Samarqand markazidagi qulay xususiy bog'cha.",
        "location_address": "Samarqand sh., Registon ko'chasi 28",
        "phone": "+998 91 540 12 03",
        "ages": "2-7 yosh",
        "capacity": 90,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "CCTV kuzatuv", "Transport", "Tibbiy xizmat"],
        "gallery": [img("quyoshcha-1"), img("quyoshcha-2"), img("quyoshcha-3")],
        "full_description": (
            "Quyoshcha bog'chasi bolalarning har tomonlama rivojlanishiga e'tibor qaratadi: "
            "til o'rganish, ijodkorlik va jismoniy faollik uyg'unlashtirilgan."
        ),
    },
    {
        "name": "Bobur Bog'i",
        "region": "Andijon",
        "district": "Andijon shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Mental arifmetika", "Shaxmat"],
        "languages": ["o'zbek", "rus"],
        "price": 850000,
        "rating": 4.4,
        "image": img("boburbogi"),
        "short_description": "Andijondagi mehribon jamoa va arzon narx.",
        "location_address": "Andijon sh., Navoiy shoh ko'chasi 56",
        "phone": "+998 99 612 77 41",
        "ages": "3-6 yosh",
        "capacity": 110,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "Tibbiy xizmat", "CCTV kuzatuv"],
        "gallery": [img("boburbogi-1"), img("boburbogi-2"), img("boburbogi-3")],
        "full_description": (
            "Bobur Bog'i — oilaviy muhit va e'tiborli tarbiyachilar bilan ajralib turadi. "
            "Mantiqiy fikrlashni rivojlantiruvchi shaxmat va mental arifmetika darslari mavjud."
        ),
    },
    {
        "name": "Smart Kids",
        "region": "Toshkent",
        "district": "Yunusobod",
        "type": "montessori",
        "programs": ["Montessori", "Robototexnika", "Ingliz tili", "Musiqa"],
        "languages": ["o'zbek", "ingliz"],
        "price": 1900000,
        "rating": 4.8,
        "image": img("smartkids"),
        "short_description": "Yunusobodda STEM va Montessori yo'nalishi.",
        "location_address": "Toshkent sh., Yunusobod tumani, Amir Temur shoh ko'chasi 210",
        "phone": "+998 93 444 21 19",
        "ages": "2-7 yosh",
        "capacity": 75,
        "hours": HOURS_FULL,
        "features": ["STEM xona", "Ingliz tilida muloqot", "Konditsioner", "CCTV kuzatuv", "Transport"],
        "gallery": [img("smartkids-1"), img("smartkids-2"), img("smartkids-3")],
        "full_description": (
            "Smart Kids bolalarni texnologiyaga do'st muhitda tarbiyalaydi. "
            "Robototexnika va Montessori metodikasi uyg'unlashtirilgan."
        ),
    },
    {
        "name": "Sehrli Olam",
        "region": "Buxoro",
        "district": "Buxoro shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Rasm chizish", "Ingliz tili"],
        "languages": ["o'zbek", "rus"],
        "price": 780000,
        "rating": 4.2,
        "image": img("sehrliolam"),
        "short_description": "Buxorodagi ijodiy yo'nalishdagi bog'cha.",
        "location_address": "Buxoro sh., Mustaqillik ko'chasi 9",
        "phone": "+998 90 718 33 06",
        "ages": "3-7 yosh",
        "capacity": 95,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "Tibbiy xizmat", "CCTV kuzatuv"],
        "gallery": [img("sehrliolam-1"), img("sehrliolam-2"), img("sehrliolam-3")],
        "full_description": (
            "Sehrli Olam bolalarning ijodiy qobiliyatlarini ochishga yo'naltirilgan. "
            "Rasm chizish, ertaklar va rolli o'yinlar orqali rivojlanish."
        ),
    },
    {
        "name": "Kelajak",
        "region": "Namangan",
        "district": "Namangan shahri",
        "type": "davlat",
        "programs": ["Maktabga tayyorlov", "Musiqa", "Sport"],
        "languages": ["o'zbek"],
        "price": 380000,
        "rating": 4.0,
        "image": img("kelajak"),
        "short_description": "Namangandagi qulay narxli davlat bog'chasi.",
        "location_address": "Namangan sh., Uychi ko'chasi 41",
        "phone": "+998 69 227 55 18",
        "ages": "3-7 yosh",
        "capacity": 160,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat (3 mahal)", "Tibbiy xizmat", "O'yin maydonchasi"],
        "gallery": [img("kelajak-1"), img("kelajak-2"), img("kelajak-3")],
        "full_description": (
            "Kelajak davlat bog'chasi keng hudud va sport maydonchalariga ega. "
            "Bolalarning sog'lom o'sishi va jamoaviy ko'nikmalariga e'tibor beriladi."
        ),
    },
    {
        "name": "Happy Baby",
        "region": "Toshkent",
        "district": "Sergeli",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Ingliz tili", "Raqs", "Mental arifmetika"],
        "languages": ["o'zbek", "rus", "ingliz"],
        "price": 1300000,
        "rating": 4.7,
        "image": img("happybaby"),
        "short_description": "Sergelidagi zamonaviy va shinam bog'cha.",
        "location_address": "Toshkent sh., Sergeli tumani, Yangi Sergeli 4-kvartal",
        "phone": "+998 97 123 09 87",
        "ages": "2-7 yosh",
        "capacity": 100,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "Ingliz tilida muloqot", "Konditsioner", "Transport", "CCTV kuzatuv", "Tibbiy xizmat"],
        "gallery": [img("happybaby-1"), img("happybaby-2"), img("happybaby-3")],
        "full_description": (
            "Happy Baby — bolalar uchun quvonchli va xavfsiz makon. "
            "Raqs, til va mantiqiy o'yinlar bilan to'la kun dasturi."
        ),
    },
    {
        "name": "Bilimdon",
        "region": "Farg'ona",
        "district": "Farg'ona shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Ingliz tili", "Shaxmat", "Rasm chizish"],
        "languages": ["o'zbek", "rus"],
        "price": 900000,
        "rating": 4.5,
        "image": img("bilimdon"),
        "short_description": "Farg'onadagi bilimga yo'naltirilgan bog'cha.",
        "location_address": "Farg'ona sh., Al-Farg'oniy ko'chasi 73",
        "phone": "+998 91 330 64 12",
        "ages": "3-7 yosh",
        "capacity": 120,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "CCTV kuzatuv", "Transport", "Tibbiy xizmat"],
        "gallery": [img("bilimdon-1"), img("bilimdon-2"), img("bilimdon-3")],
        "full_description": (
            "Bilimdon bog'chasi maktabga puxta tayyorgarlikka ixtisoslashgan. "
            "O'qish, yozish va mantiqiy fikrlash ko'nikmalari erta yoshdan shakllantiriladi."
        ),
    },
    {
        "name": "Oltin Beshik",
        "region": "Qoraqalpog'iston",
        "district": "Nukus shahri",
        "type": "davlat",
        "programs": ["Maktabga tayyorlov", "Musiqa", "Rasm chizish"],
        "languages": ["o'zbek", "qoraqalpoq"],
        "price": 350000,
        "rating": 4.1,
        "image": img("oltinbeshik"),
        "short_description": "Nukusdagi mehribon davlat bog'chasi.",
        "location_address": "Nukus sh., Doslik ko'chasi 15",
        "phone": "+998 61 222 41 77",
        "ages": "3-7 yosh",
        "capacity": 140,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat (3 mahal)", "Tibbiy xizmat", "O'yin maydonchasi"],
        "gallery": [img("oltinbeshik-1"), img("oltinbeshik-2"), img("oltinbeshik-3")],
        "full_description": (
            "Oltin Beshik bog'chasi mahalliy madaniyat va tilga e'tibor qaratadi. "
            "Bolalar quvnoq va e'tiborli muhitda tarbiyalanadi."
        ),
    },
    {
        "name": "Umid",
        "region": "Qashqadaryo",
        "district": "Qarshi shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Ingliz tili", "Mental arifmetika"],
        "languages": ["o'zbek", "rus"],
        "price": 720000,
        "rating": 4.3,
        "image": img("umid"),
        "short_description": "Qarshidagi qulay va ishonchli bog'cha.",
        "location_address": "Qarshi sh., Mustaqillik ko'chasi 102",
        "phone": "+998 90 655 18 24",
        "ages": "3-6 yosh",
        "capacity": 85,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "CCTV kuzatuv", "Tibbiy xizmat"],
        "gallery": [img("umid-1"), img("umid-2"), img("umid-3")],
        "full_description": (
            "Umid bog'chasi bolalarning bilim va ko'nikmalarini bosqichma-bosqich rivojlantiradi. "
            "Iliq munosabat va xavfsiz sharoit ta'minlangan."
        ),
    },
    {
        "name": "Nilufar",
        "region": "Xorazm",
        "district": "Urganch shahri",
        "type": "davlat",
        "programs": ["Maktabga tayyorlov", "Musiqa", "Sport"],
        "languages": ["o'zbek"],
        "price": 400000,
        "rating": 4.0,
        "image": img("nilufar"),
        "short_description": "Urganchdagi keng hududli davlat bog'chasi.",
        "location_address": "Urganch sh., Al-Xorazmiy ko'chasi 33",
        "phone": "+998 62 224 90 51",
        "ages": "3-7 yosh",
        "capacity": 150,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat (3 mahal)", "Tibbiy xizmat", "O'yin maydonchasi"],
        "gallery": [img("nilufar-1"), img("nilufar-2"), img("nilufar-3")],
        "full_description": (
            "Nilufar bog'chasida bolalar sport va musiqa orqali har tomonlama rivojlanadi. "
            "Tajribali tarbiyachilar jamoasi faoliyat yuritadi."
        ),
    },
    {
        "name": "Montessori House",
        "region": "Toshkent",
        "district": "Yakkasaroy",
        "type": "montessori",
        "programs": ["Montessori", "Ingliz tili", "Musiqa", "Rasm chizish"],
        "languages": ["o'zbek", "ingliz", "rus"],
        "price": 2500000,
        "rating": 5.0,
        "image": img("montessorihouse"),
        "short_description": "Yakkasaroydagi premium Montessori bog'chasi.",
        "location_address": "Toshkent sh., Yakkasaroy tumani, Shota Rustaveli ko'chasi 18",
        "phone": "+998 90 100 50 50",
        "ages": "1.5-6 yosh",
        "capacity": 50,
        "hours": HOURS_FULL,
        "features": ["Bassein", "Ingliz tilida muloqot", "STEM xona", "Organik ovqat", "Konditsioner", "Transport", "Tibbiy xizmat", "CCTV kuzatuv"],
        "gallery": [img("montessorihouse-1"), img("montessorihouse-2"), img("montessorihouse-3")],
        "full_description": (
            "Montessori House — eng yuqori darajadagi xizmat va sertifikatlangan murabbiylar. "
            "Bolaning tabiiy qiziqishiga asoslangan individual ta'lim dasturi."
        ),
    },
    {
        "name": "Yulduzcha",
        "region": "Jizzax",
        "district": "Jizzax shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Ingliz tili", "Rasm chizish"],
        "languages": ["o'zbek", "rus"],
        "price": 680000,
        "rating": 4.2,
        "image": img("yulduzcha"),
        "short_description": "Jizzaxdagi qulay narxli xususiy bog'cha.",
        "location_address": "Jizzax sh., Sharof Rashidov ko'chasi 47",
        "phone": "+998 72 226 13 90",
        "ages": "3-7 yosh",
        "capacity": 90,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "CCTV kuzatuv", "Tibbiy xizmat"],
        "gallery": [img("yulduzcha-1"), img("yulduzcha-2"), img("yulduzcha-3")],
        "full_description": (
            "Yulduzcha bog'chasi bolalarga sifatli ta'lim va g'amxo'rlik taqdim etadi. "
            "Quvnoq muhit va e'tiborli tarbiyachilar."
        ),
    },
    {
        "name": "Aqlvoy",
        "region": "Sirdaryo",
        "district": "Guliston shahri",
        "type": "xususiy",
        "programs": ["Maktabga tayyorlov", "Mental arifmetika", "Shaxmat", "Ingliz tili"],
        "languages": ["o'zbek", "rus"],
        "price": 750000,
        "rating": 4.4,
        "image": img("aqlvoy"),
        "short_description": "Gulistondagi mantiqiy rivojlanishga yo'naltirilgan bog'cha.",
        "location_address": "Guliston sh., Istiqlol ko'chasi 21",
        "phone": "+998 67 235 47 62",
        "ages": "3-6 yosh",
        "capacity": 80,
        "hours": HOURS_FULL,
        "features": ["Issiq ovqat", "O'yin maydonchasi", "CCTV kuzatuv", "Transport", "Tibbiy xizmat"],
        "gallery": [img("aqlvoy-1"), img("aqlvoy-2"), img("aqlvoy-3")],
        "full_description": (
            "Aqlvoy bog'chasi bolalarning aqliy rivojlanishiga alohida e'tibor beradi. "
            "Mental arifmetika va shaxmat orqali fikrlashni o'stiradi."
        ),
    },
    {
        "name": "Bahor",
        "region": "Surxondaryo",
        "district": "Termiz shahri",
        "type": "davlat",
        "programs": ["Maktabga tayyorlov", "Musiqa", "Rasm chizish"],
        "languages": ["o'zbek"],
        "price": 360000,
        "rating": 4.0,
        "image": img("bahor"),
        "short_description": "Termizdagi tajribali davlat bog'chasi.",
        "location_address": "Termiz sh., Al-Hakim at-Termiziy ko'chasi 8",
        "phone": "+998 76 227 38 14",
        "ages": "3-7 yosh",
        "capacity": 130,
        "hours": HOURS_WEEKDAY,
        "features": ["Issiq ovqat (3 mahal)", "Tibbiy xizmat", "O'yin maydonchasi"],
        "gallery": [img("bahor-1"), img("bahor-2"), img("bahor-3")],
        "full_description": (
            "Bahor bog'chasi bolalarga issiq va g'amxo'r muhit taqdim etadi. "
            "Musiqa va ijod orqali rivojlanishga e'tibor qaratiladi."
        ),
    },
]


# Ba'zi bog'chalar uchun namuna sharhlar (kalit — bog'cha nomi)
REVIEWS = {
    "Little Genius": [
        {"name": "Dilnoza A.", "text": "Bolam ingliz tilini juda tez o'rgandi. Tarbiyachilar mehribon.", "rating": 5.0},
        {"name": "Sardor M.", "text": "Narxi balandroq, lekin sifatga arziydi.", "rating": 4.5},
    ],
    "Montessori House": [
        {"name": "Kamola T.", "text": "Eng yaxshi bog'cha! Individual yondashuv juda zo'r.", "rating": 5.0},
    ],
    "Gulxan": [
        {"name": "Nodir R.", "text": "Davlat bog'chasi uchun yaxshi. Ovqati mazali.", "rating": 4.0},
        {"name": "Madina S.", "text": "Hudud keng, bolalarga qulay.", "rating": 4.5},
    ],
    "Happy Baby": [
        {"name": "Aziza K.", "text": "Raqs darslari bolamga juda yoqdi.", "rating": 5.0},
    ],
}


def seed(reset: bool = False) -> None:
    db = SessionLocal()
    try:
        if reset:
            deleted = db.query(models.Kindergarten).delete()
            db.commit()
            print(f"O'chirildi: {deleted} ta bog'cha (va ularning sharhlari).")

        added = 0
        skipped = 0
        reviews_added = 0

        for data in KINDERGARTENS:
            exists = (
                db.query(models.Kindergarten)
                .filter(models.Kindergarten.name == data["name"])
                .first()
            )
            if exists:
                skipped += 1
                continue

            kg = models.Kindergarten(**data)
            db.add(kg)
            db.flush()  # kg.id ni olish uchun

            for r in REVIEWS.get(data["name"], []):
                db.add(models.Review(kindergarten_id=kg.id, **r))
                reviews_added += 1

            added += 1

        db.commit()

        total = db.query(models.Kindergarten).count()
        print(f"Qo'shildi: {added} ta bog'cha, {reviews_added} ta sharh.")
        if skipped:
            print(f"O'tkazib yuborildi (allaqachon mavjud): {skipped} ta.")
        print(f"Bazadagi jami bog'chalar: {total} ta.")
    finally:
        db.close()


if __name__ == "__main__":
    seed(reset="--reset" in sys.argv)