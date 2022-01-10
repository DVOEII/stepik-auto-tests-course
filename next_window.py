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

    #input_value
    input_value = browser.find_element(By.ID, 'input_value')
    x = input_value.text
    answer = browser.find_element(By.ID, "answer").send_keys(calc(x))

    # submit
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
