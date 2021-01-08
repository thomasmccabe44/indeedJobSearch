from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def web_deverloper():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.indeed.com/jobs?q=Front+End+Web+Developer&l=Lowell%2C+MA&fromage=7')

    # from Get url request take url convert to text
    html_text = requests.get('https://www.indeed.com/jobs?q=Front+End+Web+Developer&l=Lowell%2C+MA&fromage=7').text
    soup = BeautifulSoup(html_text, 'lxml')
    # Find a job using param1 tagname param two className(s), convert to text
    job = soup.find('h2', class_='title').text
    print(job)
    

web_deverloper()