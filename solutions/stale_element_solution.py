"""Tests Hidden Element Page"""
from selenium import webdriver
from selenium.common import exceptions
import time

from stale_element_lib import *

def my_click_action(driver):
    
    btn = driver.find_element_by_css_selector('#main-table > tbody > tr:nth-child(1) button')
    btn.click()
    # print(btn.text) # To verify I get the element definitely 


    # --- Wrong Exmaple: Repeatedly re-operate on manipulated objects ---
    # for i in range(1, 9):
    #     btn = driver.find_element_by_css_selector(f'#main-table > tbody > tr:nth-child({i}) button')
    #     btn.click()

def my_sendkey_and_checked_action(driver):
    inp = driver.find_element_by_css_selector('#exampleInputPassword')
    inp.send_keys('password filled !')

    chk = driver.find_element_by_css_selector('#exampleCheck')
    chk.click()


if __name__ == '__main__':
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://localhost:5000/stale_element')
    
    time.sleep(7)

    for i in range(1, 8+1):

        # Use Build-In Method
        repeat_action(click_action, chrome_driver, {'click': f'#main-table > tbody > tr:nth-child({i}) button'}, 5)
        #repeat_action(checkbox_action, chrome_driver, {'checkbox': '#exampleCheck'}, 5)
        #repeat_action(sendkeys_action, chrome_driver, {'sendkeys': '#exampleInputPassword', 'text': 'password'}, 5)
        #break

        # Wrong Example 1: Build-In function With Wrong Key (Dictionary KeyError)
        #repeat_action(click_action, chrome_driver, {'c': f'#main-table > tbody > tr:nth-child({i}) button'}, 5)
        #break

        # Wrong Example 2: No_Such_Element Exception
        #repeat_action(click_action, chrome_driver, {'click': f'#main-table > tbody > tr:nth-child(777) button'}, 5)
        #break


        # Use Personal Method
        #repeat_action(my_click_action, chrome_driver, {}, 5)
        #repeat_action(my_sendkey_and_checked_action, chrome_driver, {}, 5)
        #break


