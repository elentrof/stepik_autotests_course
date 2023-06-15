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
    browser.get("http://suninjuly.github.io/alert_accept.html")

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text

    y = calc(x)

    ans = browser.find_element(By.ID, 'answer').send_keys(y)
    submt = browser.find_element(By.TAG_NAME, 'button')
    submt.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
