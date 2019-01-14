#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver      #从selenium导入webdriver
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')

#by_id
driver.find_element_by_id("kw").send_keys("seleniummmmm")
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(5)
driver.quit()