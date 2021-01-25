from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
import re
import sys
from bs4 import BeautifulSoup as soup


def login(browser):
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys("demo_python_test")
    password_input.send_keys("demo_python")
    print("Logged in Sucess")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(5)


def get_message(browser):
    insta_temp = {}
    while True:
        insta = {}
        chat = browser.page_source
        cont = soup(chat, "html.parser").prettify()
        cont_search = soup(chat, "html.parser")
        account_name = cont_search.findAll("div", attrs={"class": "_7UhW9 xLCgt qyrsm KV-D4 fDxYl"})
        account_message = cont_search.findAll("span", attrs={"class": "_7UhW9 xLCgt qyrsm KV-D4 se6yk"})

        for i in range(0, len(re.findall("_41V_T Sapc9 Igw0E IwRSH eGOV_ _4EzTm", cont))):
            insta[account_name[i].text] = account_message[i].text

        print(insta.values(), insta_temp.values())

        print("dict ", insta)
        print("Number of unread messages", len(re.findall("_41V_T Sapc9 Igw0E IwRSH eGOV_ _4EzTm", cont)))
        print("Web browser Profile", browser.firefox_profile)



if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')

    sleep(4)
    try:
        login(browser)
        print("starting")
        not_now = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

        not_now2 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

        sleep(4)
        browser.get("https://www.instagram.com/direct/inbox/")
        not_now = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        sleep(4)

    except:
        print("refresh again and try")

    get_message(browser)



# browser.close()
