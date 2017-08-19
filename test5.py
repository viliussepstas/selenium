from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path_to_chromedriver = '/Users/Vilius/Desktop/python/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://jobs.theguardian.com/jobs/finance-and-accounting/#browsing'
mainurl = driver.current_url
next_page = driver.find_element_by_xpath('''//*[@id="main"]/div/div/div[2]/div[9]/ul/li[7]/a/i''')

def get_headers(driver):
    url = 'https://jobs.theguardian.com/jobs/finance-and-accounting/#browsing'
    header_list = driver.find_elements_by_class_name('lister__view-details')

    for header in header_list:
	    driver.get(header.get_attribute("href"))

    if driver.find_elements_by_xpath('//h1'):
    print driver.find_elements_by_xpath('//h1').text
    else
    print "null"
    driver.get(mainurl)
