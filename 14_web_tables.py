# -*- coding: utf-8 -*-
"""
Description: Working with web tables like extracting data and counting rows and columns.
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/Users/aditipc/Desktop/Python_Practice/HTML_table.html")

# To find number of rows in table
rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))

# To find number of theads in a table i.e. counting number of columns
columns = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("Rows:", rows, "Columns:", columns)

# To read the data from the HTML Table i.e. all rows and columns
for r in range(2,rows+1):
    for c in range(1,columns+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="\t")
    print("\n")
