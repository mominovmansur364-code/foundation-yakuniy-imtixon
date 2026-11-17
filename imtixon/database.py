import sqlite3

db=sqlite3.connect("imtixon/malumotlar.db")
cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS malumotlar(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    iqtibos_matn TEXT,
    muallif VARCHAR(60),
    kategoriya VARCHAR(60),
    sana varchar(60),
    sevimli varchar(50)
);
""")
print("Muvaffaqiyatli table yaratildi!")
db.commit()
