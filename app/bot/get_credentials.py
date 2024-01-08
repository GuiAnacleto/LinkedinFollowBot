##Classe que tenha funções que permitem pegar credencias em tempo de execução.
##Esses metodos tem que proteger a senha ao digitar.
##Ela deve retornar um dicionario contendo as credenciais.

from getpass4 import getpass

class Credentials:
    def __init__(self, username = "", password = ""):
        self.__username = username
        self.__password = password

    def get_credentials(self):
        self.__username = input("Digite o seu username: ")
        self.__password = getpass("Digite a sua senha: ")
        return {"username": self.__username, "password": self.__password}