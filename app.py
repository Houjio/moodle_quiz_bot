from selenium.webdriver import Firefox
import pandas as pd
import os
from pathlib import Path
from time import sleep
from answer import answers

# TODO fini le cours de tensor flow pour pas avoir besoin des reponses

pth = str(Path(__file__).absolute().parent.absolute())

URL = 'https://moodle.polymtl.ca/mod/quiz/view.php?id=414414'

try:
    with open('creds.txt', 'r') as f:
        user = f.readline()
        psw = f.readline()
except FileNotFoundError:
    print("Insert t'es info avants. SVP lire le README.md")
    quit()


class Scrapper():
    def __init__(self):
        self.driver = Firefox(
            executable_path='{}/geckodriver'.format(pth))
        self.page_num = 1

    def getpage(self):
        self.driver.get('https://moodle.polymtl.ca/my/')
        sleep(7)
        # Tres lent mais moint d'erreures
        c_btn = self.driver.find_element_by_xpath(
            '/html/body/div[3]/nav/ul[2]/li[3]/div/span/a')
        c_btn.click()

    def login(self, u, p):
        u_inp = self.driver.find_element_by_xpath('//*[@id="username"]')
        u_inp.send_keys(u)
        p_inp = self.driver.find_element_by_xpath('//*[@id="password"]')
        p_inp.send_keys(p)
        log_btn = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        log_btn.click()
        sleep(7)
        if self.driver.current_url != 'https://moodle.polymtl.ca/my/':
            print("Change tes infromation car ton mot de passe n'est pas juste.")
            exit()

    def start_quiz(self, url):
        self.driver.get(url)
        sleep(2)
        s_btn = self.driver.find_elements_by_class_name('btn-secondary')[0]
        s_btn.click()
        c_btn = self.driver.find_element_by_xpath('//*[@id="id_submitbutton"]')
        c_btn.click()

    def answer_page(self):
        a_inps = self.driver.find_elements_by_css_selector('.form-control.mb-1')
        a = answers(self.page_num)
        for i in range(len(a_inps)):
            a_inps[i-1].send_keys(a[i-1])
        self.switch_page()

    def switch_page(self):
        self.page_num += 1
        s_btn = self.driver.find_elements_by_css_selector('.mod_quiz-next-nav.btn.btn-primary')
        if len(s_btn) == 0:
            pass
        else:
            s_btn[0].click()
            sleep(3)
            self.answer_page()
    
    def finish_quizz(self):
        pass

if __name__ == '__main__':
    x = Scrapper()
    x.getpage()
    x.login(user, psw)
    x.start_quiz(URL)
    x.answer_page()