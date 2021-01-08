from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.indeed.com/')

# searchbox = sb
job_sb = driver.find_element_by_name("q")
job_sb.send_keys('Front End Web Developer')
# loaction_sb = driver.find_element_by_name("l")
# loaction_sb.send_keys('Lowel, MA')
search_button = driver.find_element_by_class_name("icl-WhatWhere-button")
search_button.click()

time.sleep(5)