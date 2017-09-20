from selenium import webdriver
import selenium.webdriver.support.ui as UI
import time
import sys
import selenium
from BeautifulSoup import BeautifulSoup

path_to_chromedriver = '/Users/Vilius/Desktop/python/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://jobs.theguardian.com/jobs/finance-and-accounting/#browsing/'
driver.get(url)
list_of_links = driver.find_elements_by_class_name("button button--lister-view-details")

for link in list_of_links:
            link.click()
            text = wait.until(
                lambda driver: driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div[1]/div/div[2]/div[2]").text)

            driver.back()
