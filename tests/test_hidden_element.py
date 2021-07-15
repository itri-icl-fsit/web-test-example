"""Tests Hidden Element Page"""
from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/hidden_element')
    driver.find_element_by_id('target-btn').click()
