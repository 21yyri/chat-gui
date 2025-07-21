from datetime import datetime
from cliente import Cliente

class Mensagem:
    def __init__(self, cliente: Cliente, conteudo: str, data: datetime) -> None:
        self.cliente = cliente
        self.conteudo = conteudo
        self.data = datetime.now()


    def __repr__(self) -> str:
        return f"{self.data} {self.cliente.username}: {self.conteudo}"
