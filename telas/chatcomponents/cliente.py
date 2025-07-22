import socket

class Cliente:
    def __init__(self, username: str = None, porta: int = None) -> None:
        self.porta = porta

        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect(('localhost', self.porta))

        self.username = username

   
    def enviar_bytes(self, msg):
        self.cliente.send(msg.encode())


    def receber_bytes(self):
        return self.cliente.recv(1024).decode()
        