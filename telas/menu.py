import customtkinter as ctk
from chatcomponents.cliente import Cliente

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.title("Menu")
        self.update_idletasks()

        self.appChat = app

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"340x140+{x}+{y}")

        self.big_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        
        self.porta = 9998
        
        self.escolha_label = ctk.CTkLabel(self, text="Grupos disponíveis.", font=self.big_font)
        self.escolha_label.pack(pady=10)
        
        self.menu = ctk.CTkOptionMenu(self, values=["Sala Um", "Sala Dois", "Sala Três"], command=self.select_port)
        self.menu.pack()

        self.botao_start = ctk.CTkButton(self, text="Entrar", command=self.join_server)
        self.botao_start.pack(pady=10)

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
        self.fechar_menu()
        self.appChat.show_login(cliente)
    
    
    def fechar_menu(self):
        self.destroy()
        

if __name__ == "__main__":
    Menu()