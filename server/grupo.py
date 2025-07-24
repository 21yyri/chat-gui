import argparse, socket
from threading import Thread, Lock

class Grupo:
    def __init__(self, port: int):
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.bind(('localhost', self.port))
        except Exception as E:
            print(E)


        self.server.listen(15)

        self.clientes = []
        self.lock = Lock()

        print(f"Servidor rodando na porta {self.port}.")

        
    def broadcast(self, mensagem):
        with self.lock:
            for cliente in self.clientes:
                try:
                    cliente.send(mensagem)
                except:
                    self.clientes.remove(cliente)


    def handle_clients(self, cliente: socket.socket):
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


    def handle_conn(self):
        while True:
            client, addr = self.server.accept()
            with self.lock:
                self.clientes.append(client)
            print(f'Conexão estabelecida com {addr}')

            threadBc = Thread(target=self.handle_clients, args=(client,))
            threadBc.start()


parser = argparse.ArgumentParser()
parser.add_argument("run", help="Escolha a porta do servidor que deseja se conectar.", type=int)

args = parser.parse_args()

if args.run < 9998 or args.run > 10000 or not isinstance(args.run, int):
    print("Escolha uma porta que seja um número inteiro entre [9998, 9999, 10000].")
else:
    servidor = Grupo(args.run)
    servidor.handle_conn()
