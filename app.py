import customtkinter as ctk
from telas.login import Login
from telas.chat import Chat

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self):
        self.show_login()
    
    def show_login(self, porta):
        self.login_window = Login(self)
        self.login_window.mainloop()

    def show_chat(self, cliente):
        self.login_window.destroy()
                
        self.chat_window = Chat(cliente)
        self.chat_window.mainloop()

if __name__ == '__main__':
    App()

