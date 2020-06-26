from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase): 
	def test_1(self):
		self.assertEqual("Congratulations! You have successfully registered!", registr("http://suninjuly.github.io/registration1.html"), "test_1_registration_failed")
		
	def test_2(self):
		self.assertEqual("Congratulations! You have successfully registered!", registr("http://suninjuly.github.io/registration2.html"), "test_2_registration_failed")

def registr(link):
	browser = webdriver.Chrome() 
	browser.get(link)
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
	return welcome_text	

if __name__ == "__main__":
    unittest.main()



