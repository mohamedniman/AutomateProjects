import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('disable-infobars')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
path = 'Documents/Projects/MyProjects/'
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
browser.get('https://github.com/login')

def create():
   folderName = str(sys.argv[1])
#    if folderName in path:
#        folderName = input('Folder Already Exist Please Enter New One? ')
#        os.mkdir(path, folderName)
#    else:
#         os.mkdir(path, folderName)
   python_button = browser.find_element_by_xpath('//*[@id="login_field"]')
   python_button.send_keys('mohamedniman')
   python_button = browser.find_element_by_xpath("//*[@id='password']")
   python_button.send_keys('maamiza9785')
   python_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]")
   python_button.click()
   browser.get('https://github.com/new')
   python_button = browser.find_element_by_xpath('//*[@id="repository_name"]')
   python_button.send_keys(folderName)
   python_button = browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
   python_button.submit()
   browser.quit()
if __name__ == '__main__':
    create()

