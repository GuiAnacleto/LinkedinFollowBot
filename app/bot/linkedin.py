#acessar o linkedin --
#logar no linkedin --
#seguir as pessoas
#mandar mensagem apresentação.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .get_credentials import Credentials

class Linkedin:
    def __init__(self, ) -> None:
        self.options= webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options)
        self.credentials = Credentials()
        credentials = self.credentials.get_credentials()
        self.username = credentials['username']
        self.password = credentials['password'] 

        
    def loginLinkedin(self):
        self.driver.get("https://www.linkedin.com/login/pt")
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        btn_enter = self.driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
        username.send_keys(self.username)
        password.send_keys(self.password)
        btn_enter.click()
        print("clicou login!!")


    def followPeople(self):
        self.driver.get("https://www.linkedin.com/search/results/people/?keywords=engenheiro%20de%20software&origin=SWITCH_SEARCH_VERTICAL&sid=!L*")
        time.sleep(10)
        while True:
            buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'artdeco-button artdeco-button--2 artdeco-button--secondary ember-view')]")
            for btn in buttons:
                if btn.text != "Enviar mensagem":
                    btn.click()
                    time.sleep(2)
                    try:
                        connect_btn = self.driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1')]")
                        connect_btn.click()
                        print("fez uma conexão!")
                    except:
                        pass
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            next_page = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Avançar')]")
            next_page.click()
            print("avançou pagina!")
            time.sleep(6)


    def sendMessage(self):
        pass