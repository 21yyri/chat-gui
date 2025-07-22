import customtkinter as ctk
from login import Login
from chat import Chat
from menu import Menu
import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (username, senha)")
cursor.execute("CREATE TABLE IF NOT EXISTS mensagens (username, conteudo, data, grupo)")
conn.commit()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self):
        self.show_menu()
    
    
    def show_menu(self):
        self.menu = Menu(self)
        self.menu.mainloop()
    
    
    def show_login(self, cliente):
        self.login_window = Login(self, cliente)
        self.login_window.mainloop()


    def show_chat(self, cliente):
        self.login_window.destroy()
                
        self.chat_window = Chat(cliente)
        self.chat_window.mainloop()


if __name__ == '__main__':
    App()
