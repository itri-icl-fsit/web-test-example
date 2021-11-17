"""Tests Hidden Element Page"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from stale_element_lib import *

import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/hidden_element2')

    # === for go to the top ===
    # driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    # time.sleep(5)

    # === Click Basic Script ===
    #btn = driver.find_element_by_id('target-btn')
    #driver.find_element_by_id('target-btn').click()
    #driver.execute_script("arguments[0].click();", btn)
 
    # === Experiment ===
    try:
        # === p=1 ===
        click_hidden_by_selector(driver, {'click': '#target-btn'})
        next_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "next-btn"))
        )
        next_btn.click()

        # === p=2 ===
        click_hidden_by_selector(driver, {'click': '#target-btn'})
        next_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "next-btn"))
        )
        next_btn.click()

        # === p=3 ===
        btn_p3 = driver.find_elements_by_css_selector('a.dropdown-item.dropdown-item-warning')[0]
        driver.execute_script("arguments[0].click();", btn_p3)
        next_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "next-btn"))
        )
        next_btn.click()

        # === p=4 ===
        click_hidden_by_selector(driver, {'click': '#target-checkbox'})
        next_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "next-btn"))
        )
        next_btn.click()

        # === p=5 ===
        click_hidden_by_xpath(driver, {'click': "//select/option[text()='Click Me!']"})
        print('last')
    finally :
        print('complete')