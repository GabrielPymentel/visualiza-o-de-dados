from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_FILE = 'temperatura.db'

# 🚀 Cria o banco se não existir
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS temperatura (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            horario DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# 🛠 Inicializa ao rodar
init_db()

# 📥 Rota que o ESP32 chama via POST
@app.route('/enviar', methods=['POST'])
def receber_dados():
    try:
        dados = request.get_json()
        temperatura = dados.get("temp")

        if temperatura is not None:
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO temperatura (valor) VALUES (?)", (temperatura,))
            conn.commit()
            conn.close()
            return jsonify({"status": "sucesso", "temp": temperatura}), 200
        else:
            return jsonify({"erro": "Dados incompletos"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ✅ Rota opcional para testar
@app.route('/')
def home():
    return "API Flask online e recebendo dados."

# 📊 Rota para ver dados (útil pro Streamlit)
@app.route('/listar')
def listar_dados():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM temperatura ORDER BY horario DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# ▶️ Roda o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
