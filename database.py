import sqlite3


def init_db():
    # Veritabanı bağlantısı oluşturma
    conn = sqlite3.connect('notlar.db')
    c = conn.cursor()

    # Notlar tablosunu oluşturma
    c.execute('''CREATE TABLE IF NOT EXISTS notlar
                (id INTEGER PRIMARY KEY,
                baslik TEXT,
                icerik TEXT,
                olusturma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    # Veritabanı işlemlerini kaydetme ve bağlantıyı kapatma
    conn.commit()
    conn.close()
