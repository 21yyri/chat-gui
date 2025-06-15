import customtkinter as ctk
from chat.cliente import Cliente

class Login(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.appChat = app
        self.title("Login")
        self.update_idletasks()

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"300x120+{x}+{y}")

        self.nomeLabel = ctk.CTkLabel(self, text="Insira o nome a ser usado no chat.")
        self.nomeLabel.pack(pady=5)

        self.entryName = ctk.CTkEntry(self)
        self.entryName.pack(pady=2)

        self.botaoLogin = ctk.CTkButton(self, text="Definir", command=self.get_name)
        self.botaoLogin.pack(pady=0)
        
        self.entryName.bind("<Return>", command = lambda e : self.get_name())

        self.botaoLogin.focus_set()
        

    def get_name(self):
        username = self.entryName.get().strip()
        if username:
            cliente = Cliente(username)
            self.appChat.show_chat(cliente)


    def fechar_login(self):
        self.destroy()


