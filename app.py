import os
from re import search
from app.bot.get_credentials import Credentials
from app.bot.linkedin import Linkedin
from app.bot.search_key import escrever_arquivo_texto
from webdriver_auto_update.chrome_app_utils import ChromeAppUtils
from webdriver_auto_update.webdriver_manager import WebDriverManager

if __name__ == "__main__":


    bot = Linkedin()
    while True:
        os.system('cls')
        print("************************************************* ROBO DO LINKEDIN *************************************************/n")
        print("1 - Alterar Chave de Busca/n")
        print("2 - Seguir Pessoas/n")
        print("3 - Sair/n")
        op = input("Digite o Numero da Sua opção: ")

        if op == '1':
            searchkey = input("Cole o link de busca e digite enter: ")
            escrever_arquivo_texto(searchkey)
        elif op == '2':
            bot.loginLinkedin()
            input("Aprove o Login no seu CELULAR e clique ENTER.")
            bot.followPeople()
        elif op == '3':
            break
    
    
    
    
