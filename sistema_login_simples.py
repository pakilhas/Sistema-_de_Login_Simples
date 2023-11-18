import getpass

def ler_usuarios(): #funcao para le o arquivo user.txt e armazena em um dicionarios chaves são os usuarios e os valores a senha
	usuarios = {}
	with open ("users.txt", "r") as file:
		for linha in file:
			usuario, senha = linha.strip().split(":")
			usuarios[usuario] = senha
	return usuarios

def registrar_usuario (usuario, senha): #funcao para adicionar novo usuario ao arquivo users.txt, recebe usuario e  senha e adiciona no final do arquivo
	with open ("users.txt", "a") as file:
		file.write(f"{usuario}:{senha}\n")

def login (): #funcao para fazer login tres vezes, caso seja faça login TRUE, caso contrario FALSE
	tentativas = 3
	usuarios = ler_usuarios() 

	while tentativas > 0:
		usuario = input ("Digite seu nome de usuario: ")
		senha = getpass.getpass("Digite sua senha: ")
		
		if usuario in usuarios and usuarios[usuario] == senha:
			print ("Login bem-sucedido!")
			return True
		else: 
			print ("Nome do usuario ou senha incorretos. Tente novamente.")
			tentativas -= 1

	print ("Nome maximo de tentativas atingidos. Saindo.")
	return False

if __name__ == "__main__":
	print ("Bem vindo ao Sistema de Login!")
	
	opcao = input ("Digite 1 para fazer login ou 2 para se registar: ")

	if opcao == "1":
		if login():
			print ("Acesso permitido")
	elif opcao == "2":
		novo_usuario = input ("Digite um novo nome de usuario: ")
		nova_senha = getpass.getpass ("Digite uma nova senha: ")
		registrar_usuario(novo_usuario, nova_senha) 
		print ("Usuario registrado com sucesso")


	else:
		print ("Opção inválida. Saindo. ")
