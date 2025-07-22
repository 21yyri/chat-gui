import customtkinter as ctk
from chatcomponents.cliente import Cliente
import json, sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

class Login(ctk.CTk):
    def __init__(self, app, cliente: Cliente):
        super().__init__()
        self.appChat = app
        self.title("Login")
        self.update_idletasks()
        
        self.cliente = cliente

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"500x320+{x}+{y}")

        self.big_font = ctk.CTkFont(family="Arial", size=24, weight="bold")

        self.nome_label = ctk.CTkLabel(self, text="Insira o nome a ser usado no chat.", font=self.big_font)
        self.nome_label.pack(pady=5)

        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.pack(pady=2)

        self.entry_senha = ctk.CTkEntry(self)
        self.entry_senha.pack(pady=2)
        self.entry_name.bind("<Return>", command = lambda e: self.get_user())

        self.botao_login = ctk.CTkButton(
            self, text="Definir", command=self.get_user
        )
        self.botao_login.pack(pady=0)

        self.botao_login.focus_set()


    def get_user(self):
        username = self.entry_name.get().strip()
        senha = self.entry_senha.get().strip()

        usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()
        for usuario in usuarios:
            if username == usuario[0] and senha == usuario[1]:
                self.cliente.username = username
                self.appChat.show_chat(self.cliente)
                break

        self.erro_label = ctk.CTkLabel(self, text="Usuario ou senha incorretos.")
        self.erro_label.pack(pady=5)

        self.registrar_label = ctk.CTkLabel(self, text="Registrar usuario?")
        self.registrar_label.pack()

        self.registrar_button = ctk.CTkButton(self, text="Registrar", command=lambda: self.registrar_user(username, senha))
        self.registrar_button.pack(pady=5)


    def registrar_user(self, username, senha):
        cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (username, senha))
        conn.commit()

        self.cliente.username = username
        self.appChat.show_chat(self.cliente)


    def fechar_login(self):
        self.destroy()
