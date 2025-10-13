from selenium import webdriver
import time 

driver = webdriver.Chrome()

driver.get('https://www.letras.mus.br/delinquent-habits/445996/')

time.sleep(10)

driver.maximize_window()

driver.quit