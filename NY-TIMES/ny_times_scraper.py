"""
Created on Thu Jun 25 2020
@author: Rupak Karki (@rupakkarki27)
"""

"""
NewYork Times search Result Scraper
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import pandas as pd


def ny_scraper(url_to_site, total_results, sleep_time):
	title = []
	date_published = []
	author = []
	category = []
	lead_paragraph = []
	url = []
	
	clicks = int(total_results / 10)
	
	
	# initialize webdriver
	driver = webdriver.Firefox()
	driver.get(url_to_site)
	
	# Clicking the 'Show More' button before scraping the data
	for i in range(clicks):
		try:
			time.sleep(3)
			driver.find_element_by_xpath('(//button[contains(.,"Show More")])').click()
		except NoSuchElementException:
			print("No show more button found!!")
			sys.exit(1)
	print("Starting to Scrape....")
	
	
	# Collecting titles
	try:
		titles = driver.find_elements_by_xpath('(//h4[@class="css-2fgx4k"])')
	except NoSuchElementException:
		print("No title element found.")
		sys.exit(1)
	for item in titles:
		title.append(item.text)
	
	# Collecting Date published
	try:
		dates = driver.find_elements_by_xpath('(//time[@class="css-17ubb9w"])')
	except NoSuchElementException:
		print("No Date element found.")
		sys.exit(1)
	for item in dates:
		date_published.append(item.text)
	
	# Collecting Category
	try:
		categories = driver.find_elements_by_xpath('(//p[@class="css-myxawk"])')
	except NoSuchElementException:
		print("No Category element found.")
		sys.exit(1)
	for item in categories:
		category.append(item.text)	

	# Collecting Lead Paragraph
	try:
		paragraphs = driver.find_elements_by_xpath('(//p[@class="css-16nhkrn"])')
	except NoSuchElementException:
		print("No paragraph element found.")
		sys.exit(1)
	for item in paragraphs:
		lead_paragraph.append(item.text)

	# Collecting the URL to that article
	try:
		links = driver.find_elements_by_css_selector("li.css-1l4w6pd a")
	except NoSuchElementException:
		print("No URL element found.")
		sys.exit(1)
	for item in links:
		url.append(item.get_attribute("href"))

	print("Title: {}".format(len(title)))
	time.sleep(3)
	print("Date: {}".format(len(date_published)))
	time.sleep(3)
	print("Category: {}".format(len(category)))
	time.sleep(3)
	print("Lead Paragraph: {}".format(len(lead_paragraph)))
	time.sleep(3)
	print("URL: {}".format(len(url)))

	# Joining together our data
	ny_times = {'Title': title,
			    'Date': date_published,
				'Category': category,
				'Lead Paragraph': lead_paragraph,
				'URL': url}
	
	return pd.DataFrame(ny_times)