from selenium.common import exceptions

def click_hidden_by_selector(driver, dict_arg):
    try:
        btn = driver.find_element_by_css_selector(dict_arg['click'])
        driver.execute_script("arguments[0].click();", btn)
    except KeyError as e:
        print('\n**********\n[Dictionary KeyError]:', e ,'(key) not found !\n(You need to set \'click\' as key)\n**********', flush=True)

def click_hidden_by_xpath(driver, dict_arg):
    try:
        btn = driver.find_element_by_xpath(dict_arg['click'])
        driver.execute_script("arguments[0].click();", btn)
    except KeyError as e:
        print('\n**********\n[Dictionary KeyError]:', e ,'(key) not found !\n(You need to set \'click\' as key)\n**********', flush=True)
