# -*- coding: utf-8 -*-
"""
Description: Working with mouse actions.
               -> Mouse Hover
               -> Double Click
               -> Right Click
               -> Drag and Drop
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usermgnt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

# Creating an object for actions chains class
actions = ActionChains(driver)

# This will mouse over admin and usermgnt element and click over users
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HTML10"]/div[1]/button')))

# To perform double click action on a button
actions.double_click(element).perform()

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

rtclick = driver.find_element_by_xpath('//*[@id="authentication"]/span')

# To perform right click
actions.context_click(rtclick).perform()


driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element = driver.find_element_by_xpath('//*[@id="box6"]')
target_element = driver.find_element_by_xpath('//*[@id="box106"]')

actions.drag_and_drop(source_element, target_element).perform()

time.sleep(5)

driver.close()
