from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

# Stworzenie instancji klasy Chrome
# (to otworzy przeglądarkę)
driver = Chrome()
# Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")

# Maksymalizacja okna
driver.maximize_window()

# Znajdz element Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# Kliknij w odnaleziony element
sleep(5)
sign_in_a.click()

email_create = driver.find_element(By.ID,"email_create").send_keys("Test@test.pl")
sleep(5)
# kliknij w button creat account
create_account = driver.find_element(By.ID,"SubmitCreate").click()
sleep(5)
zaznacz_checkboxa = driver.find_element(By.NAME, "id_gender").click()
print(type(sign_in_a))
sleep(5)
driver.quit()

sleep(5)
driver.quit()
