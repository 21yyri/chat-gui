import socket
from threading import Thread, Lock

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(('localhost', 9998))
except Exception as E:
    print(E)


server.listen(15)

clientes = []
lock = Lock()

def broadcast(mensagem: bytearray):
    print(type(mensagem))
    print(mensagem.decode())
    with lock:
        for cliente in clientes:
            try:
                cliente.send(mensagem)
            except:
                clientes.remove(cliente)

def handle_clients(cliente: socket.socket):
    while True:
        try:
            msg = cliente.recv(1024)
            if not msg:
                break
            broadcast(msg)
        except:
            with lock:
                clientes.remove(cliente)
                cliente.close()

def handle_conn():
    while True:
        client, addr = server.accept()
        with lock:
            clientes.append(client)
        print(f'Conexão estabelecida com {addr}')

        threadBc = Thread(target=handle_clients, args=(client,))
        threadBc.start()


print('Iniciando servidor.')
handle_conn()
