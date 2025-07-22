from datetime import datetime
from .cliente import Cliente

class Mensagem:
    def __init__(self, cliente: str, conteudo: str, data: datetime = datetime.now().time()) -> None:
        self.cliente = cliente
        self.conteudo = conteudo
        self.data = f"{data.hour}:{data.minute}"


    def __str__(self) -> str:
        return f"[{self.data}] {self.cliente}: {self.conteudo}\n"
