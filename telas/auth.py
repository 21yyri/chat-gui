import customtkinter as ctk
import requests
import sqlite3

def validar_username(username):
    ...

def validar_senha(username):
    ...


def registrar():
    ...


def logar():
    ...


class Auth(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Autenticação")
        self.geometry("400x200")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.auth_label = ctk.CTkLabel(self, text="Chat GUI", font=("", 26, "bold"))
        self.auth_label.pack(pady=25)

        self.registrar_button = ctk.CTkButton(self, text="Registrar", command=registrar)
        self.registrar_button.pack(pady=10)

        self.logar_button = ctk.CTkButton(self, text="Logar", command=logar)
        self.logar_button.pack(pady=10)


if __name__ == '__main__':
    app = Auth()
    app.mainloop()