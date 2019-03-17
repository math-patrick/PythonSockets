#! python2

# Imports
import socket
import hashlib

# Informacoes do socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Informacoes de login - comum
contaComum = hashlib.md5('user').hexdigest() # Conta do usuario
senhaComum = hashlib.md5('123').hexdigest() # Senha do usuario

# Informacoes de login - admin
contaAdmin = hashlib.md5('admin').hexdigest() # Conta do admin
senhaAdmin = hashlib.md5('124').hexdigest() # Senha do admin

# Funcao responsavel por receber a mensagem
def receiveMessage(con):
	msg = con.recv (1024)
	return msg

# Funcao responsavel por verificar se a senha funciona
def checkPassword(password, type):
	if (type == 1):
		if (password == senhaComum):
			print 'Senha correta! Bem vindo Sylveon'
			return True
		else:
			print 'Senha incorreta! Finalizando...'
			return False
	else:
		if (password == senhaAdmin):
			print 'Senha incorreta! Bem vindo Vaporeon!'
			return True
		else:
			print 'Senha incorreta! Finalizando...'
			return False

# Funcao responsavel pelo login
def checkLogin(con):
	msg = receiveMessage(con)
	if not msg: 
		return False
	if (msg == contaComum):
		print 'Logando como usuario comum. Por favor digite sua senha: '
		msg = receiveMessage(con)
		return checkPassword(msg, 1)
	if (msg == contaAdmin):
		print 'Logando como administrador/ Por favor digite sua senha: '
		msg = receiveMessage(con)
		return checkPassword(msg, 2)
	else:
		print 'Usuario nao encontrado. Finalizando conexao.'
		return False
# Dados da conexao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

# Inicia a conexao
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    conexao = True
    while conexao:
    	conexao = checkLogin(con)   
    print 'Finalizando conexao do cliente', cliente
    con.close()