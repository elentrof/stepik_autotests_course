from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, 'input_value')
    x = int(x.text)
    y = calc(x)

    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    chkbx = browser.find_element(By.ID, 'robotCheckbox')
    chkbx.click()

    chkbx = browser.find_element(By.ID, 'robotsRule')
    chkbx.click()

    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
