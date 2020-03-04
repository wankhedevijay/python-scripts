from selenium import webdriver
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://twitter.com/')

username_box = driver.find_element_by_class_name('r-30o5oe')
username_box.send_keys(username)

password_box = driver.find_element_by_class_name('r-30o5oe')
password_box.send_keys(password)

login_button = driver.find_element_by_role('button')
login_button.submit()

driver.close()