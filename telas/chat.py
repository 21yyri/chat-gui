import customtkinter as ctk
from threading import Thread
from chatcomponents.mensagem import Mensagem
from chatcomponents.cliente import Cliente
from datetime import datetime
import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

class Chat(ctk.CTk):
    def __init__(self, cliente: Cliente):
        super().__init__()
        self.cliente = cliente

        self.title(self.cliente.username)
        self.update_idletasks()

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 600) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"600x400+{x}+{y}")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.fechar_chat)

        match self.cliente.porta:
            case 9998:
                self.grupo = 1
            case 9999:
                self.grupo = 2
            case 10000:
                self.grupo = 3

        self.chat_display = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.chat_display.pack(fill="both", expand=True, padx=20, pady=10)

        self.msg_entry = ctk.CTkEntry(self, width=500, height=30)
        self.msg_entry.pack(side="left", fill='x', padx=10, pady=5)
        self.msg_entry.bind("<Return>", lambda event : self.send_mensagem())

        self.enviar = ctk.CTkButton(self, text="Enviar", command=self.send_mensagem)
        self.enviar.pack(side="right", padx=5, pady=0)

        mensagens = cursor.execute(f"SELECT * FROM mensagens WHERE grupo = {self.grupo}").fetchall()
        if mensagens != []:
            for mensagem in mensagens:
                self.atualizar_display(f"[{mensagem[2]}] {mensagem[0]}: {mensagem[1]}\n")

        self.receber_thread = Thread(target=self.receber_mensagem, daemon=True)
        self.receber_thread.start()


    def send_mensagem(self):
        mensagem: str = f"{self.cliente.username};{self.msg_entry.get()}"
        if mensagem:
            self.cliente.enviar_bytes(mensagem)
            self.msg_entry.delete(0, 'end')


    def receber_mensagem(self):
        while True:
            try:
                mensagem: str = self.cliente.receber_bytes().split(";")
                mensagem: Mensagem = Mensagem(mensagem[0], mensagem[1])

                cursor.execute("INSERT INTO mensagens (username, conteudo, data, grupo) VALUES (?, ?, ?, ?)", 
                               (mensagem.cliente, mensagem.conteudo, mensagem.data, self.grupo))
                conn.commit()

                self.atualizar_display(mensagem.__str__())
            except Exception as e:
                print(e)


    def atualizar_display(self, mensagem):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", mensagem)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")


    def fechar_chat(self):
        self.destroy()
