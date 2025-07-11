import customtkinter as ctk

class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chatroom menu")
        self.update_idletasks()

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - 300) // 2
        y = (screen_h - 400) // 2

        self.geometry(f"500x500+{x}+{y}")


        self.escolha_label = ctk.CTkLabel(self, text="Escolha o servidor a logar.").grid(row=0, column=0)

        self.grupo_um = ctk.CTkButton(self, text="Sala Um").grid(row=1, column=0)

        self.grupo_dois = ctk.CTkButton(self, text="Sala Dois").grid(row=1, column=1)

        self.grupo_tres = ctk.CTkButton(self, text="Sala Tres").grid(row=1, column=2)

        self.mainloop()


if __name__ == "__main__":
    Menu()