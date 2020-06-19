from time import sleep
from selenium import webdriver
from ultra_secreto import usuario
from ultra_secreto import clave



class Bot():
	def __init__(self,usuario,clave):
		self.driver = webdriver.Firefox()
		self.driver.get('https://www.instagram.com')
		sleep(5)
		self.driver.find_element_by_name('username')\
			.send_keys(usuario)
		self.driver.find_element_by_name('password')\
			.send_keys(clave)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
			.click()
		
my_confidence = Bot(usuario,clave)
