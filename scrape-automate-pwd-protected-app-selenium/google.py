from selenium import webdriver

browser = webdriver.Chrome()
url = "http://google.com"
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
<textarea name='??'><textarea>
<input name="q" type="text">
"""