from datetime import datetime

class Mensagem:
    def __init__(self, cliente: str, conteudo: str, data: datetime = datetime.now().time()) -> None:
        self.cliente = cliente
        self.conteudo = conteudo

        if data.hour < 10:
            hora = f"0{data.hour}"
        else:
            hora = data.hour
        if data.minute < 10:
            minuto = f"0{data.minute}"
        else:
            minuto = data.minute

        self.data = f"{hora}:{minuto}"


    def __str__(self) -> str:
        return f"[{self.data}] {self.cliente}: {self.conteudo}\n"
