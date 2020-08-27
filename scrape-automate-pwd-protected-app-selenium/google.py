from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://google.com"
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
<textarea name='??'><textarea>
<input name="q" type="text">
"""

time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name("q") 
# print(search_el)
# search_el = browser.find_elements_by_css_selector("h1")
search_el.send_keys("selenium python") # this will input the search terms

"""
<input type='submit' />
<button type='submit' />
<form></form>
<input type="submit">
"""
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']") #find the submit buttion 
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()