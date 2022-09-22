from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from os import system, name as osname
from random import randrange

## Opening link and logging in
def login(link,email,passwd):
    ## Initialising/Installing Chromedriver
    global driver, flag, templink
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
    if (link != templink):
            print("Loading Discord...")
            driver.get(link)
            templink = link
    if (flag == False):
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME , 'email')))
        print("\nLogging in...")
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(passwd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(3)
        print("\nLogged in successfully")
        flag = True
    sleep(1)

## Send messages
def send_messages(n,messages):
    for i in range(n):
        for message in messages:
            actions = ActionChains(driver)

            # posts message
            actions.send_keys(message)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            # interval between messages in seconds
            sleep(120)
    print("\nAll Messages Sent")

## Menu
def main():
    global flag
    flag = False

    # discord email and password
    email,passwd = "", ""

    while True:
        # discord url in string format
        link = ''

        # list of messages to post
        messages = []

        # number of loops to run
        n = 1000
        print()

        # login to discord
        login(link,email,passwd)

        # loop through list of messages n times
        send_messages(n,messages)
        break

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()
