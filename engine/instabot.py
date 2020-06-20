from time import sleep
from selenium import webdriver
from ultra_secreto import usuario
from ultra_secreto import clave



class Bot:
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

