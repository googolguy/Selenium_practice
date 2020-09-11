# -*- coding: utf-8 -*-
"""
Description: How to download a file.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To download the file to user defined location otherwise it will download to default download folder
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "‪C:\\Users\\aditipc\\Documents"})

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe", chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("Test Data for file download")
driver.find_element_by_id("createTxt").click()  # Generate file

driver.find_element_by_xpath('//*[@id="link-to-download"]').click()  # File download


