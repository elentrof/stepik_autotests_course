from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    btn = browser.find_element(By.TAG_NAME, 'button')
    el = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn.click()
    x = browser.find_element(By.ID, 'input_value').text

    y = calc(x)

    ans = browser.find_element(By.ID, 'answer').send_keys(y)
    submt = browser.find_element(By.ID, 'solve')
    submt.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
