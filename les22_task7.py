from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Ivan')

    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Petrov')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('asd@asd.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
