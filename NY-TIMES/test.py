# Titles
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

titles = driver.find_elements_by_xpath('(//h4[@class="css-2fgx4k"])')

for item in titles:
	print(item.text)

# Date_published
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

times = driver.find_elements_by_xpath('(//time[@class="css-17ubb9w"])')

for item in times:
	print(item.text)


# Category
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

categories = driver.find_elements_by_xpath('(//p[@class="css-myxawk"])')

for item in categories:
	print(item.text)

# Lead Paragraph
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

paragraphs = driver.find_elements_by_xpath('(//p[@class="css-16nhkrn"])')

for item in paragraphs:
	print(item.text)
	
# URL
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

links = driver.find_elements_by_css_selector("li.css-1l4w6pd a")
for link in links:
    print(link.get_attribute("href"))
	
# Clicking Show More
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

# trying to click 5 times
for i in range(5):
	time.sleep(3)
	driver.find_element_by_xpath('(//button[contains(.,"Show More")])').click()


# Author
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
authors = []
authors_list = []
driver = webdriver.Firefox()
driver.get('https://www.nytimes.com/search?dropmab=false&query=Machine%20Learning&sort=newest')

for i in range(6):
	time.sleep(3)
	driver.find_element_by_xpath('(//button[contains(.,"Show More")])').click()

result_cards = driver.find_elements_by_css_selector('li.css-1l4w6pd')

for item in result_cards:
    try:
        author = item.find_elements_by_xpath('(//p[@class="css-15w69y9"])')
        authors.append(author)
    except NoSuchElementException:
        print("No author found for this")
        authors.append(-1)

auth = authors[0]
print(len(auth))

for item in auth:
	print(item.text)