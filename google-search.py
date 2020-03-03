from selenium import webdriver
from getpass import getpass

print('Hello Wankhede!')

search = input('Search: ')

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://www.google.com/')

search_box = driver.find_element_by_name('q')
search_box.send_keys(search)

search_button = driver.find_element_by_name('btnK')
search_button.submit()

index = 0
while index < 2:
  search_box = driver.find_element_by_name('q')
  search_box.clear()

  search = input('Search: ')

  search_box = driver.find_element_by_name('q')
  search_box.send_keys(search)

  search_button = driver.find_element_by_class_name('Tg7LZd')
  search_button.submit()
  index += 1

driver.get('https://vijaywankhede.wordpress.com/about/')
# driver.close()