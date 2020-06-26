from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase): 
	link1 = "http://suninjuly.github.io/registration1.html"
	browser = webdriver.Chrome() 
	browser.get(link1)
	input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @placeholder='Input your first name']")
	input1.send_keys("Мой ответ")
	input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @placeholder='Input your last name']")
	input2.send_keys("Мой ответ") 
	input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @placeholder='Input your email']")
	input3.send_keys("Мой ответ") 
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text
	def test_1(self):
		self.assertEqual("Congratulations! You have successfully registered!", "welcome_text", "Not successefully registered_1")
	link2 = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link2)
	input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @placeholder='Input your first name']")
	input1.send_keys("Мой ответ") 
	input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @placeholder='Input your email']")
	input3.send_keys("Мой ответ") 
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text
	def test_2(self):
		self.assertEqual("Congratulations! You have successfully registered!", "welcome_text", "Not successefully registered_2")
if __name__ == "__main__":
    unittest.main()


