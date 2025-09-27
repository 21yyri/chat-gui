# chat-gui
Um chat desktop com autenticação simples, persistência de mensagens e rooms para diálogo rápido com usuários simultâneos.

Projeto entregue na matéria de Programação Orientada a Objetos e desenvolvido com o intuito de aprender a projetar e criar interfaces gráficas desktop e estudar a comunicação por meio de protocolos de rede como o TCP via sockets.

## Instalação
``pip install -r requirements.txt``

A aplicação depende do customtkinter para sua interface. Todas as outras bibliotecas utilizadas são nativas ao Python moderno.

## Passo a passo
Na tela inicial, a aplicação pedirá um usuário e uma senha. Caso ainda não tenha logado, pode criar a partir dessa tela. Os dados vão ser salvos num banco SQLite.

Em uma tela posterior, o usuário deve decidir a que sala quer se conectar, tendo três opções que vão definir a que porta do localhost será feita a conexão.

Por fim, a tela do chat aparecerá, permitindo o envio de mensagens, formatadas com data, nome de usuário e mensagem enviada.
