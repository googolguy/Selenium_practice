# -*- coding: utf-8 -*-
"""
Description: Working with Radio buttons and Check Boxes.
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
second_driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Working with radio buttons
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

button_before = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input').is_selected()
print("Radio button selected: ", button_before)

driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input').click()

button_after = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input').is_selected()
print("Radio button selected: ", button_after)

# Working with Check boxes
second_driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

checkbox1_before = second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input').is_selected()
checkbox2_before = second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input').is_selected()
print("Check Box 1 selected:", checkbox1_before, ", Check Box 2 selected:", checkbox2_before)

second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input').click()
second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input').click()

checkbox1_after = second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input').is_selected()
checkbox2_after = second_driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input').is_selected()
print("Check Box 1 selected:", checkbox1_after, ", Check Box 2 selected:", checkbox2_after)