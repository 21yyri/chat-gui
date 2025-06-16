from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('flask/database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome, senha)")

# CRIAR UMA ROTA PARA VERIFICAR SE USUARIO REGISTIRANDO JA EXISTE E CRIAR UM JSON COMO RESPOSTA
app.route('/registrar_usuario')
def registrar_user():
    usuario = request.get_json()
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (usuario.nome, usuario.senha))

