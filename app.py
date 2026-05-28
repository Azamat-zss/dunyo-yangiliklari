from flask import Flask, render_template, abort

app = Flask(__name__)

# Barcha yangiliklar ma'lumotlar bazasi (tasodifiy xatoliklarsiz, toza ma'lumotlar)
yangiliklar_royxati = [
    {
        "id": 1,
        "sarlavha": "O'zbekistonda raqamli texnologiyalar rivojlanishi yangi bosqichga chiqdi",
        "matn": "Yurtimizda IT sohasi keskin rivojlanmoqda. Yangi loyihalar va startaplar uchun xalqaro miqyosda keng imkoniyatlar yaratilmoqda.",
        "kategoriya": "texnologiya",
        "vaqt": "Bugun, 12:00"
    },
    {
        "id": 2,
        "sarlavha": "Jahon chempionati: Milliy terma jamoamiz g'alaba qozondi!",
        "matn": "Kecha bo'lib o'tgan shiddatli o'yinda futbolchilarimiz ajoyib o'yin ko'rsatib, muhim g'alabani qo'lga kiritishdi va muxlislarni xushnud etishdi.",
        "kategoriya": "sport",
        "vaqt": "Bugun, 10:30"
    },
    {
        "id": 3,
        "sarlavha": "Xalqaro sammitda iqtisodiy hamkorlik masalalari muhokama qilindi",
        "matn": "Bugun boshlangan global anjumanda yetakchi davlatlar vakillari yangi savdo aloqalarini o'rnatish va investitsiya kiritish masalalarini kelishib olishdi.",
        "kategoriya": "siyosat",
        "vaqt": "Kecha, 18:45"
    }
]

@app.route('/')
def bosh_sahifa():
    # Bosh sahifaga barcha yangiliklarni yuboramiz
    return render_template('index.html', yangiliklar=yangiliklar_royxati)

@app.route('/yangilik/<int:yangilik_id>')
def batafsil_sahifa(yangilik_id):
    # ID bo'yicha kerakli yangilikni qidirib topamiz
    yangilik = next((y for y in yangiliklar_royxati if y["id"] == yangilik_id), None)
    if yangilik is None:
        abort(404) # Agar yangilik topilmasa, 404 xato oynasi chiqadi
    return render_template('batafsil.html', yangilik=yangilik)

@app.route('/kategoriya/<string:kat_nomi>')
def kategoriya_sahifasi(kat_nomi):
    # Faqat tanlangan kategoriyaga tegishli yangiliklarni saralaymiz
    saralangan = [y for y in yangiliklar_royxati if y["kategoriya"] == kat_nomi.lower()]
    return render_template('index.html', yangiliklar=saralangan)

if __name__ == '__main__':
    app.run(debug=True)
