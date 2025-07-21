import customtkinter as ctk
from chatcomponents.cliente import Cliente
from app import App

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.title("Chatroom menu")
        self.update_idletasks()

        self.appChat = app

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"340x200+{x}+{y}")

        self.big_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        
        self.porta = 9998
        
        self.escolha_label = ctk.CTkLabel(self, text="Escolha o servidor a logar.", font=self.big_font)
        self.escolha_label.pack(pady=10)

        # self.grupo_um = ctk.CTkButton(self, text="Sala Um", height=50)
        # self.grupo_dois = ctk.CTkButton(self, text="Sala Dois", height=50)
        # self.grupo_tres = ctk.CTkButton(self, text="Sala Tres", height=50)
        
        self.menu = ctk.CTkOptionMenu(self, values=["Sala Um", "Sala Dois", "Sala Três"], command=self.teste)
        self.menu.pack()

        # self.grupo_um.pack(pady=5)
        # self.grupo_dois.pack(pady=5)
        # self.grupo_tres.pack(pady=5)
        self.mainloop()

    def select_port(self, escolha):
        match escolha:
            case "Sala Um":
                self.porta = 9998
            case "Sala Dois":
                self.porta = 9999
            case "Sala Três":
                self.porta = 10000


    def join_server(self):
        cliente = Cliente(porta=self.porta)
        self.appChat.show_login(cliente)
    
    
    def fechar_menu(self):
        self.destroy()
        

if __name__ == "__main__":
    Menu()