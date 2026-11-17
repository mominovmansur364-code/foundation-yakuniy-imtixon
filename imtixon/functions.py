from database import db,cursor
from datetime import datetime
from groq import Groq
from secret import API_KEY

def add_quote(matn,muallif,kategoriya,sevimli=True):
    sana=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO malumotlar(iqtibos_matn,muallif,kategoriya,sana,sevimli)
    VALUES(?,?,?,?,?)
""",(matn,muallif,kategoriya,sana,sevimli))

    db.commit()
    print("Muvaffaqiyatli saqlandi!")

def show_quotes():
    cursor.execute("SELECT * FROM malumotlar")
    natija=cursor.fetchall()

    if not natija:
        print("Hozircha ma'lumotlar yo'q!")
    
    else:
        print("====BARCHA IQTIBOSLAR====")
        for i in natija:
            print(f"Iqtibos ID si: {i[0]}")
            print(f"Iqtibosni matni: {i[1]}")
            print(f"Muallifi: {i[2]}")
            print(f"Kategoriyasi: {i[3]}")
            print(f"Sanasi: {i[4]}")
            print(f"Sevimlilarga qo'shilganmi:  {"Ha" if str(i[5]) == "1" else "Yo'q"}")
            print("="*20)

def update_quote(aydi,matn,muallif,kategoriya,sevimli=True):
    cursor.execute("""
    UPDATE malumotlar
    SET iqtibos_matn = ?, muallif = ?, kategoriya = ?, sevimli = ?
    WHERE id = ?
""",(matn, muallif, kategoriya, sevimli, aydi))

    db.commit()

    if cursor.rowcount==0:
        print("Bunday ID li iqtibos topilmadi!")
    else:
        print("Muvaffaqiyatli yangilandi!")

def delete_quote(aydi):
    cursor.execute("DELETE FROM malumotlar  WHERE id=?",(aydi, ))

    db.commit()

    if cursor.rowcount==0:
        print("Bunday ID li iqtibos topilmadi!")
    else:
        print("Muvaffaqiyatli o'chirildi!")

def search_quote(aydi):
    cursor.execute("SELECT * FROM malumotlar WHERE id=?",(aydi, ))

    natija=cursor.fetchone()

    if natija is None:
        print("Bunday ID li iqtibos topilmadi!")
    else:
        print("=====Iqtibos haqida=====")
        print(f"Iqtibos ID si: {natija[0]}")
        print(f"Iqtibos matni: {natija[1]}")
        print(f"Iqtibos muallifi: {natija[2]}")
        print(f"Iqtibos kategoriyasi: {natija[3]}")
        print(f"Sanasi: {natija[4]}")
        print(f"Sevimlilarga qo'shilganmi:  {"Ha" if str(natija[5]) == "1" else "Yo'q"}")




def AI():
    sorov = input("Qanday yordam kerak: ").strip()

    if not sorov:
        print("So'rov bo'sh bo'lishi mumkin emas!")
        return

    system_prompt = "Sen AYTI o'qituvchisisan. Faqat shu faningga aloqador savollarga javob ber, aks holda rad et."

    try:
        client = Groq(api_key=API_KEY)
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": sorov},
            ],
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            reasoning_effort="medium",
            stream=True,
            stop=None,
        )

        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="", flush=True)
        print()

    except KeyboardInterrupt:
        print("\nJavob to'xtatildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")