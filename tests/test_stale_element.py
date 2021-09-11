"""Tests Hidden Element Page"""
from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/stale_element')
    for i in range(1, 8+1):
        driver.find_element_by_css_selector(f'#main-table > tbody > tr:nth-child({i}) button').click()
