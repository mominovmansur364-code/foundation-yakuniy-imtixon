from functions import *

def ha_yoqmi(savol):
    javob = input(savol).strip().lower()
    if javob == "":
        return True
    return javob in ("ha", "h", "y", "yes", "1")

while True:
    print("\n=====MENYU=====")
    print("""1.Iqtibos qo'shish
2.Barcha iqtiboslarni ko'rish
3.ID bo'yicha iqtibosni yangilash
4.ID bo'yicha iqtibosni o'chirish
5.ID bo'yicha iqtibosni qidirish
6.Boshqa yordam
0.Chiqish""")
    print("="*20)
    try:
        tanlov=int(input("\nTanlang: "))
    except ValueError:
        print("Iltimos faqat raqam kiriting")
        continue

    if tanlov==1:
        matn=input("Iqtibos matnini kiriting: ")
        muallif=input("Iqtibosni muallifi: ")
        kategoriya=input("Kategoriyasi: ")
        sevimli = ha_yoqmi("Sevimlilarga qo'shiladimi? (ha/yo'q, bo'sh = ha): ")
        add_quote(matn,muallif,kategoriya,sevimli)
    elif tanlov==2:
        show_quotes()

    elif tanlov==3:
        try:
            aydi=int(input("Yangilaydigan iqtibosingizni ID si: "))
        except ValueError:
            print("Id faqat raqamda bo'lishi shart!")
            continue
        matn = input("Yangi matn: ")
        muallif = input("Yangi muallif: ")
        kategoriya = input("Yangi kategoriya: ")
        sevimli = ha_yoqmi("Sevimlilarga qo'shiladimi? (ha/yo'q, bo'sh = ha): ")
        update_quote(aydi, matn, muallif, kategoriya, sevimli)

    elif tanlov==4:
        try:
            aydi=int(input("O'chiradigan iqtibosingizni ID sini kiriting: "))
        except ValueError:
            print("Id faqat raqamda bo'lishi shart!")
            continue
        delete_quote(aydi)

    elif tanlov==5:
        try:
            aydi=int(input("Qidirayotgan iqtibosingizni ID sini kiritng: "))
        except ValueError:
            print("ID faqat raqamda bo'lishi shart!")
            continue
        search_quote(aydi)

    elif tanlov==6:
        AI()

    elif tanlov==0:
        print("Dastur tugatildi!")
        break
    else:
        print("Notog'ri tanlov faqat 0 dan 6 gacha raqam tanlang!")