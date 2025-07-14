import socket
from threading import Thread, Lock


class Grupo:
    def __init__(self, porta: int) -> None:
        self.porta = porta

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", self.porta))

        self.server.listen(25)

        self.clientes = []
        self.lock = Lock()

        self.handle_conn()

    def broadcast(self, mensagem: bytes) -> None:
        with self.lock:
            for cliente in self.clientes:
                try:
                    cliente.send(mensagem)
                except:
                    self.clientes.remove(cliente)


    def handle_clients(self, cliente: socket.socket) -> None:
        while True:
            try:
                msg = cliente.recv(1024)
                if not msg:
                    break
                self.broadcast(msg)
            except:
                with self.lock:
                    self.clientes.remove(cliente)
                    cliente.close()


    def handle_conn(self) -> None:
        while True:
            client, addr = self.server.accept()
            with self.lock:
                self.clientes.append(client)
            print(f'Conexão estabelecida com {addr}')

            threadBc = Thread(target=self.handle_clients, args=(client,))
            threadBc.start()


class GrupoUm(Grupo):
    def __init__(self, porta: int = 9999) -> None:
        super().__init__(porta)


class GrupoDois(Grupo):
    def __init__(self, porta: int = 9998) -> None:
        super().__init__(porta)


class GrupoTres(Grupo):
    def __init__(self, porta: int = 9997) -> None:
        super().__init__(porta)
