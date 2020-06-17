import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


input1 = browser.find_element_by_id("answer")
input1.send_keys(y) 

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

browser.execute_script("window.scrollBy(0, 100);")
option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_tag_name("button")
button.click()

assert True