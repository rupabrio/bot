from time import sleep
from selenium import webdriver
from random import randint


class Bot:
    def __init__(self, user, password):
        self.user = user
        self.pw = password
        self.driver = webdriver.Firefox()
        self.mouth = "Can't talk"

    def logfile(self, to_log):
        with open('./logs.txt', 'a') as f:
            f.write(f"{to_log}\n")

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
        sleep(3)
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

    def log_out(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button")\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[9]')\
            .click()

    def go_to_post(self, post_id):
        sleep(randint(4, 6))
        self.driver.get(f"https://www.instagram.com/p/{post_id}")

    def like(self):
        sleep(randint(4, 6))
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg')\
            .click()

    def like_post(self, post_id):
        try:
            self.go_to_post(post_id)
            self.like()
            self.logfile(f"{post_id} liked")
        except:
            self.logfile(f"{post_id} not liked")

    def like_posts(self, post_list):
        for post_id in post_list:
            like_post(post_id)

    def exit(self):
        self.log_out()
        sleep(3)
        self.driver.close()
