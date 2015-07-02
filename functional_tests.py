from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

page_body = browser.find_element_by_tag_name('body')
assert 'It Worked!' in page_body.text

browser.quit()