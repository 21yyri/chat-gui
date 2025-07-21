import socket, pickle

class msg:
    def __init__(self, conteudo):
        self.conteudo = conteudo

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 9998))

msge = msg("oii")

cliente.send(pickle.dumps(msge))
cliente.close()