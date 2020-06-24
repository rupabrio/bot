from time import sleep
from selenium import webdriver
from random import randint

class Bot:
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

   def likes(self): #Auto-likes en fotos random
	

    def exit(self):
        self.driver.close()
