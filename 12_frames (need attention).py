# -*- coding: utf-8 -*-
"""
Description: Working with frames.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/documentation/en/")

