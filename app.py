from flask import Flask, render_template, abort
import random

app = Flask(__name__)

# Dunyo yangiliklari uchun mukammal shablonlar
DAVLATLAR = ["AQSh", "Yaponiya", "Germaniya", "Xitoy", "Buyuk Britaniya", "Fransiya", "Janubiy Koreya", "Braziliya", "BAA", "Turkiya"]
TEXNO_MAVZU = ["yangi kvant kompyuteri", "uchar elektromobillar", "shaffof smartfon", "6G aloqa tarmog'i", "sun'iy intellektli robotlar"]
SPORT_MAVZU = ["Futbol bo'yicha Jahon Chempionati", "Formula-1 poygalari", "Xalqaro Marafon", "Kiber-sport turniri", "Olimpiada o'yinlari"]
SIYOSAT_MAVZU = ["Iqlim o'zgarishi bo'yicha xalqaro sammit", "Yangi iqtisodiy ittifoq shartnomasi", "Kosmik dasturlarni moliyalashtirish", "Yashil energiya global forumi"]

def cheksiz_yangiliklar_yarat():
    """Har safar sayt ochilganda 45 ta mutlaqo turli xil dunyo yangiliklarini yaratadi"""
    baza = []
    
    # 1. Texnologiya yangiliklari
    for i in range(1, 16):
        davlat = random.choice(DAVLATLAR)
        mavzu = random.choice(TEXNO_MAVZU)
        baza.append({
            "id": i,
            "kategoriya": "texnologiya",
            "sarlavha": f"{davlat} davlatida taqdim etilgan {mavzu} dunyoni hayratda qoldirdi",
            "vaqt": f"Bugun, {random.randint(10, 23)}:{random.randint(10, 59)}",
            "matn": "Dunyo olimlari va texnologiya gigantlari ushbu yangilikni asr kashfiyoti deb atashmoqda.",
            "batafsil_matn": f"{davlat} hududida o'tkazilgan maxsus yopiq taqdimotda yetakchi muhandislar tomonidan yaratilgan {mavzu} namoyish etildi. Ushbu loyiha ustida mutaxassislar deyarli 5 yildan beri ishlashayotgan edi. Ushbu texnologiya yaqin kelajakda insoniyat hayotini, iqtisodiyotni va kundalik turmush tarzini butunlay o'zgartirib yuborishi kutilmoqda. Hozirda yirik korporatsiyalar ushbu loyihaga milliardlab dollar investitsiya kiritishni boshladi."
        })
        
    # 2. Sport yangiliklari
    for i in range(16, 31):
        davlat = random.choice(DAVLATLAR)
        mavzu = random.choice(SPORT_MAVZU)
        baza.append({
            "id": i,
            "kategoriya": "sport",
            "sarlavha": f"{davlat} hududida o'tkazilayotgan {mavzu} kutilmagan g'alabalar bilan boshlandi",
            "vaqt": f"Kecha, {random.randint(10, 23)}:{random.randint(10, 59)}",
            "matn": "Dunyoning eng kuchli sportchilari va jamoalari ushbu turnirda g'alaba uchun kurashmoqda.",
            "batafsil_matn": f"Butun dunyo muxlislari diqqat markazida bo'lgan {mavzu} musobaqasi {davlat} maydonlarida shiddatli ruhda davom etmoqda. Ekspertlar va tahlilchilar ushbu mavsumda mutlaqo kutilmagan g'alabalar va tarixiy rekordlar qayd etilayotganini ta'kidlashmoqda. Muxlislar o'z sevimli jamoalarini qo'llab-quvvatlash uchun dunyoning turli burchaklaridan tashrif buyurishgan. Musobaqa yakunida g'oliblar maxsus oltin kubok va yirik pul mukofotlari bilan taqdirlanadi."
        })

    # 3. Siyosat yangiliklari
    for i in range(31, 46):
        davlat = random.choice(DAVLATLAR)
        mavzu = random.choice(SIYOSAT_MAVZU)
        baza.append({
            "id": i,
            "kategoriya": "siyosat",
            "sarlavha": f"{davlat} poytaxtida bo'lib o'tgan {mavzu} muvaffaqiyatli yakunlandi",
            "vaqt": f"{random.randint(2, 4)} kun oldin",
            "matn": "Dunyo yetakchilari global muammolarni hal qilish va yangi bitimlar imzolash uchun yig'ilishdi.",
            "batafsil_matn": f"{davlat} poytaxtida tashkil etilgan {mavzu} doirasida dunyoning eng nufuzli davlatlari rahbarlari va xalqaro tashkilotlar vakillari uchrashishdi. Muzokaralar davomida xalqaro xavfsizlik, iqtisodiy hamkorlik va global inqirozlarni bartaraf etish masalalari chuqur muhokama qilindi. Uchrashuv yakunida tomonlar kelgusi o'n yillik strategik rejalarni belgilab beruvchi maxsus deklaratsiyani imzoladilar."
        })
        
    return baza

@app.route('/')
def bosh_sahifa():
    yangiliklar = cheksiz_yangiliklar_yarat()
    random.shuffle(yangiliklar)
    return render_template('index.html', yangiliklar=yangiliklar)

@app.route('/kategoriya/<nomi>')
def kategoriya_sahifasi(nomi):
    baza = cheksiz_yangiliklar_yarat()
    saralangan = [y for y in baza if y['kategoriya'] == nomi.lower()]
    return render_template('index.html', yangiliklar=saralangan)

@app.route('/yangilik/<int:yangilik_id>')
def batafsil_sahifa(yangilik_id):
    baza = cheksiz_yangiliklar_yarat()
    yangilik = next((y for y in baza if y['id'] == yangilik_id), None)
    
    if yangilik is None:
        yangilik = random.choice(baza)
        
    return render_template('batafsil.html', yangilik=yangilik)

if __name__ == '__main__':
    app.run(debug=True)