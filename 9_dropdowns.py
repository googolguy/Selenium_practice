# -*- coding: utf-8 -*-
"""
Description: Working with Dropdowns.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

# Selecting an option from dropdown
drp = Select(driver.find_element_by_name("state"))

drp.select_by_visible_text('Washington') # First method - select by visible text
drp.select_by_index(2) # Second method - select by index
# Third method - select by value

# Count number of options available
print("Options available in dropdown:", len(drp.options))

# Capture all the options and print them as output
all_options = drp.options
print("All options available in Dropdown:-")
for option in all_options:
    print(option.text)

driver.quit()