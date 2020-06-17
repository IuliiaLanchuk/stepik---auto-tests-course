from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("Smolensk")

import os 

current_dir = os.path.abspath(os.path.dirname("C:\\Users\\lanch\\selenium_course\\"))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element = browser.find_element_by_css_selector('[type="file"]')
element.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
browser.quit() 
