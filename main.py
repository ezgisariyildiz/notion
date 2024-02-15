from flask import Flask, request, jsonify
import sqlite3
import requests
from flask import Flask, render_template
import database

app = Flask(__name__)
app.static_folder = 'static'

database.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notlar', methods=['GET'])
def notlari_listele():
    conn = sqlite3.connect('notlar.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notlar")
    notlar = c.fetchall()
    conn.close()

    return jsonify(notlar)

@app.route('/notlar', methods=['POST'])
def not_ekle():
    data = request.get_json()
     # Eğer istek JSON içermiyorsa veya isteğin Content-Type'ı 'application/json' değilse hata döndür
    if not data or request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Geçersiz istek. JSON içeriği bekleniyor.'}), 415
    baslik = data['baslik']
    icerik = data['icerik']
    conn = sqlite3.connect('notlar.db')
    c = conn.cursor()
    c.execute("INSERT INTO notlar (baslik, icerik) VALUES (?, ?)", (baslik, icerik))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Not başariyla eklendi'})

@app.route('/notlar/<int:id>', methods=['GET'])
def not_getir(id):
    conn = sqlite3.connect('notlar.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notlar WHERE id = ?", (id,))
    notlar = c.fetchall()
    conn.close()

    if notlar:
        return jsonify(notlar)
    else:
        return jsonify({'error': 'Belirtilen ID ile not bulunamadı'}), 404


@app.route('/notlar/<int:id>', methods=['DELETE'])
def not_sil(id):
    conn = sqlite3.connect('notlar.db')
    c = conn.cursor()
    c.execute("DELETE FROM notlar WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Not {id} basariyla silindi'})

if __name__ == '__main__':
    app.run(debug=True)
