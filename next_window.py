from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with open('test1.txt', 'w') as file:
   file.write('test1 for mls 228')

import os
path = os.getcwd() + '/' + file.name

try:


    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    # submit
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #confirm
#    confirm = browser.switch_to.alert
#    confirm.accept()

    #input_value
    input_value = browser.find_element(By.ID, 'input_value')
    x = input_value.text
    answer = browser.find_element(By.ID, "answer").send_keys(calc(x))

    # submit
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    #intut
#    firstname = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]").send_keys('1')
#    lastname = browser.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys('1')
#    email = browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys('1')

    # file
#    current_dir = os.path.abspath(os.path.dirname(__file__))
#    file = browser.find_element(By.CSS_SELECTOR, "input[name=file]").send_keys(path)

    #robotCheckbox
#    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
#    robotCheckbox.click()

    #robotsRule
#    robotsRule = browser.find_element(By.ID, "robotsRule").click()



finally:
    time.sleep(10)
    browser.quit()