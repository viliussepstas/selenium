from selenium import webdriver

path_to_chromedriver = '/Users/Vilius/Desktop/python/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://jobs.theguardian.com/jobs/finance-and-accounting/#browsing'
post_list = driver.find_elements_by_xpath('''//*[@id="main"]/div/div/div[1]/div[1]/div/div[2]/div[2]''')
driver.get(url)
header_list = driver.find_elements_by_class_name('lister__view-details')
next_page = driver.find_element_by_xpath('''//*[@id="main"]/div/div/div[2]/div[9]/ul/li[7]/a/i''')

def get_headers(driver):
    for header in header_list:
        print [cell.text for cell in header.find_elements_by_class_name('lister__view-details')

while True:
    get_headers(driver)
