from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    img_element = browser.find_element(By.ID, 'treasure')
    x = img_element.get_attribute("valuex")
    y = calc(x)

    ans = browser.find_element(By.ID, 'answer')
    ans.send_keys(y)

    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()

    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    butt = browser.find_element(By.CSS_SELECTOR, "button.btn")
    butt.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
