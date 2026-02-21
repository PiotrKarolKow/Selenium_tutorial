from selenium import webdriver
from time import sleep

#Stworzenie instancji klasy chrome
#
driver = webdriver.Chrome()
#otworz przegladarke
driver.get("https://www.google.com")
# MAksymalizacja okna
driver.maximize_window()
sleep(5)
driver.quit()

