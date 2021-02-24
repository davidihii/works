#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

usernameStr = "votre_identifiant"
passwordStr = "votre_mdp"


def jobMatin():
    browser = webdriver.Chrome("chemin_du_fichier_chromedriver")
    browser.get(("https://adel.adrar-formation.eu/login/index.php"))

    username = browser.find_element_by_id("username")
    username.send_keys(usernameStr)

    username = browser.find_element_by_id("password")
    username.send_keys(passwordStr)

    nextButton = browser.find_element_by_id("loginbtn")
    nextButton.click()

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-site-index")))

    finally:

        browser.get(("https://adel.adrar-formation.eu/mod/chat/gui_ajax/index.php?id=403"))

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-mod-chat-gui_ajax-index")))

    finally:
        messageDuMoment = browser.find_element_by_id("input-message")
        messageDuMoment.send_keys("Bonjour !!")
        messageDuMoment.send_keys(Keys.RETURN)

    



def jobMidi():
    browser = webdriver.Chrome("/usr/local/Caskroom/chromedriver/node_modules/chromedriver/bin/chromedriver")
    browser.get(("https://adel.adrar-formation.eu/login/index.php"))

    username = browser.find_element_by_id("username")
    username.send_keys(usernameStr)

    username = browser.find_element_by_id("password")
    username.send_keys(passwordStr)

    nextButton = browser.find_element_by_id("loginbtn")
    nextButton.click()

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-site-index")))

    finally:

        browser.get(("https://adel.adrar-formation.eu/mod/chat/gui_ajax/index.php?id=403"))

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-mod-chat-gui_ajax-index")))

    finally:
        messageDuMoment = browser.find_element_by_id("input-message")
        messageDuMoment.send_keys("Bon Ap !!")
        messageDuMoment.send_keys(Keys.RETURN)


def jobAprem():
    browser = webdriver.Chrome("/usr/local/Caskroom/chromedriver/node_modules/chromedriver/bin/chromedriver")
    browser.get(("https://adel.adrar-formation.eu/login/index.php"))

    username = browser.find_element_by_id("username")
    username.send_keys(usernameStr)

    username = browser.find_element_by_id("password")
    username.send_keys(passwordStr)

    nextButton = browser.find_element_by_id("loginbtn")
    nextButton.click()

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-site-index")))

    finally:

        browser.get(("https://adel.adrar-formation.eu/mod/chat/gui_ajax/index.php?id=403"))

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-mod-chat-gui_ajax-index")))

    finally:
        messageDuMoment = browser.find_element_by_id("input-message")
        messageDuMoment.send_keys("re/re/re/re")
        messageDuMoment.send_keys(Keys.RETURN)


def jobSoir():
    browser = webdriver.Chrome("/usr/local/Caskroom/chromedriver/node_modules/chromedriver/bin/chromedriver")
    browser.get(("https://adel.adrar-formation.eu/login/index.php"))

    username = browser.find_element_by_id("username")
    username.send_keys(usernameStr)

    username = browser.find_element_by_id("password")
    username.send_keys(passwordStr)

    nextButton = browser.find_element_by_id("loginbtn")
    nextButton.click()

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-site-index")))

    finally:

        browser.get(("https://adel.adrar-formation.eu/mod/chat/gui_ajax/index.php?id=403"))

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-mod-chat-gui_ajax-index")))

    finally:
        messageDuMoment = browser.find_element_by_id("input-message")
        messageDuMoment.send_keys("Allez Ciao !!!")
        messageDuMoment.send_keys(Keys.RETURN)


def jobLaPau():
    browser = webdriver.Chrome("/usr/local/Caskroom/chromedriver/node_modules/chromedriver/bin/chromedriver")
    browser.get(("https://adel.adrar-formation.eu/login/index.php"))

    username = browser.find_element_by_id("username")
    username.send_keys(usernameStr)

    username = browser.find_element_by_id("password")
    username.send_keys(passwordStr)

    nextButton = browser.find_element_by_id("loginbtn")
    nextButton.click()

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-site-index")))

    finally:

        browser.get(("https://adel.adrar-formation.eu/mod/chat/gui_ajax/index.php?id=403"))

    try:
        waiting = WebDriverWait(browser, 10)
        element = waiting.until(EC.presence_of_element_located((By.ID, "page-mod-chat-gui_ajax-index")))

    finally:
        messageDuMoment = browser.find_element_by_id("input-message")
        messageDuMoment.send_keys("La Pause !!!")
        messageDuMoment.send_keys(Keys.RETURN)


schedule.every().monday.at("08:55").do(jobMatin)
schedule.every().monday.at("10:30").do(jobLaPau)
schedule.every().monday.at("10:45").do(jobAprem)
schedule.every().monday.at("12:30").do(jobMidi)
schedule.every().monday.at("13:27").do(jobAprem)
schedule.every().monday.at("15:30").do(jobLaPau)
schedule.every().monday.at("15:47").do(jobAprem)
schedule.every().monday.at("17:00").do(jobSoir)


schedule.every().tuesday.at("08:55").do(jobMatin)
schedule.every().tuesday.at("10:30").do(jobLaPau)
schedule.every().tuesday.at("10:45").do(jobAprem)
schedule.every().tuesday.at("12:30").do(jobMidi)
schedule.every().tuesday.at("13:27").do(jobAprem)
schedule.every().tuesday.at("15:30").do(jobLaPau)
schedule.every().tuesday.at("15:47").do(jobAprem)
schedule.every().tuesday.at("17:00").do(jobSoir)


schedule.every().wednesday.at("08:55").do(jobMatin)
schedule.every().wednesday.at("10:30").do(jobLaPau)
schedule.every().wednesday.at("10:45").do(jobAprem)
schedule.every().wednesday.at("12:30").do(jobMidi)
schedule.every().wednesday.at("13:27").do(jobAprem)
schedule.every().wednesday.at("15:30").do(jobLaPau)
schedule.every().wednesday.at("15:47").do(jobAprem)
schedule.every().wednesday.at("17:00").do(jobSoir)


schedule.every().thursday.at("08:55").do(jobMatin)
schedule.every().thursday.at("10:30").do(jobLaPau)
schedule.every().thursday.at("10:45").do(jobAprem)
schedule.every().thursday.at("12:30").do(jobMidi)
schedule.every().thursday.at("13:27").do(jobAprem)
schedule.every().thursday.at("15:30").do(jobLaPau)
schedule.every().thursday.at("15:47").do(jobAprem)
schedule.every().thursday.at("17:00").do(jobSoir)


schedule.every().friday.at("08:55").do(jobMatin)
schedule.every().friday.at("10:30").do(jobLaPau)
schedule.every().friday.at("10:45").do(jobAprem)
schedule.every().friday.at("12:30").do(jobMidi)
schedule.every().friday.at("13:27").do(jobAprem)
schedule.every().friday.at("15:00").do(jobLaPau)
schedule.every().friday.at("15:15").do(jobAprem)
schedule.every().friday.at("16:42").do(jobSoir)



while True:

    schedule.run_pending()
    time.sleep(1)


