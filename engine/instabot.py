from time import sleep
from selenium import webdriver
from random import randint


class Bot:
<<<<<<< HEAD
    def __init__(self, user, password):
        self.user = user
        self.pw = password
        self.driver = webdriver.Firefox()
        self.mouth = "Can't talk"

    def go_to(self, default="https://www.instagram.com/", user=""):
        self.driver.get(default + user)
        sleep(randint(4, 6))

    def log_in(self):
        sleep(randint(4, 6))
        self.driver.find_element_by_name('username').send_keys(self.user)
        self.driver.find_element_by_name('password').send_keys(self.pw)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(randint(4, 6))

    def skip(self):
        sleep(randint(4, 6))
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
            .click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()

    def enter(self):
        self.go_to()
        self.log_in()
        try:
            self.skip()
        except:
            print("Unable to skip")
        finally:
            print("Successfully logged in")
            sleep(randint(4, 6))
=======
	def __init__(self,usuario,clave):
		self.user = usuario
		self.pw = clave
		self.driver = webdriver.Firefox()

	def navegar(self):
		self.driver.get('https://www.instagram.com')

	def loggeo(self):
		sleep(5)
		self.driver.find_element_by_name('username')\
			.send_keys(usuario)
		self.driver.find_element_by_name('password')\
			.send_keys(clave)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
			.click()

	def skip(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
			.click()
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
			.click()


	def busqueda(self):\
		self.driver.find_element_by_name('Search')\
			.send_keys('rubebriceno')


	def entrar(self):
		self.navegar()
		sleep(5)
		self.loggeo()
		sleep(5)
		self.skip()


test = Bot(usuario,clave)
test.entrar()

>>>>>>> d95fb544ffddc79290d2899c8a8a1b41d95b6299
