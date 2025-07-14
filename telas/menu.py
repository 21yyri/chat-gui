import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chatroom menu")
        self.update_idletasks()

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"500x300+{x}+{y}")

        self.big_font = ctk.CTkFont(family="Arial", size=24, weight="bold")


        self.escolha_label = ctk.CTkLabel(self, text="Escolha o servidor a logar.", font=self.big_font)
        self.escolha_label.pack(pady=10)

        self.grupo_um = ctk.CTkButton(self, text="Sala Um", height=50)
        self.grupo_dois = ctk.CTkButton(self, text="Sala Dois", height=50)
        self.grupo_tres = ctk.CTkButton(self, text="Sala Tres", height=50)

        self.grupo_um.pack(pady=5)
        self.grupo_dois.pack(pady=5)
        self.grupo_tres.pack(pady=5)
        self.mainloop()


if __name__ == "__main__":
    Menu()