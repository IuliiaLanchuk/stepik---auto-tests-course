from selenium import webdriver
import time

def calc(x,y):
  return str(int(x)+int(y))
 
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
sum_element = calc(x,y)

from selenium.webdriver.support.ui import Select 
select=Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(sum_element))

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()
	
