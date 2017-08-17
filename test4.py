from selenium import webdriver

path_to_chromedriver = '/Users/Vilius/Desktop/python/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://jobs.theguardian.com/jobs/finance-and-accounting/#browsing'
post = driver.find_elements_by_xpath('''//*[@id="main"]/div/div/div[1]/div[1]/div/div[2]/div[2]''')

driver.get(url)

for header in driver.find_elements_by_class_name('lister__view-details'):
    header.click()
    print "------------------------------------"
    print driver.find_element_by_class_name('fix-text').text
    print "------------------------------------"
    print driver.find_element_by_xpath('''//*[@id="main"]/div/div/div[1]/div[1]/div/div[1]/div[1]/dl/div[2]/dd/span''').text
    driver.back()
