from selenium.common import exceptions

def click_action(driver, dict_arg):
    # click the element whose css selector is dict_arg['checkbox']
    try:
        btn = driver.find_element_by_css_selector(dict_arg['click'])
        btn.click()
    except KeyError as e:
        print('\n**********\n[Dictionary KeyError]:', e ,'(key) not found !\n(You need to set \'click\' as key)\n**********', flush=True)

def checkbox_action(driver, dict_arg):
    # check the element whose css selector is dict_arg['checkbox']
    try:
        chkbox = driver.find_element_by_css_selector(dict_arg['checkbox'])
        chkbox.click()
    except KeyError as e:
        print('\n**********\n[Dictionary KeyError]:', e ,'(key) not found !\n(You need to set \'checkbox\' as key)\n**********', flush=True)

def sendkeys_action(driver, dict_arg):
    # Filled dict['text'] to input element
    try:
        _input = driver.find_element_by_css_selector(dict_arg['sendkeys'])
        _input.send_keys(dict_arg['text'])
    except KeyError as e:
        print('\n**********\n[Dictionary KeyError]:', e ,'(key) not found !\n(You need to set \'sendkeys\' and \'text\' as key)\n**********', flush=True)

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


def repeat_action(action, driver, dict_arg={}, attempts=5):
    # action: a function (Function)
    # dict_arg: a collection for parameter of action function (Diciotnary)
    # attempts: retry times (Integer)
    # driver: Selenium Driver

    while attempts :
        try:
            #print("[Enter Try]")
            if dict_arg != {}:
                action(driver, dict_arg)
            else:
                action(driver)
            break
        except exceptions.StaleElementReferenceException as e:
            print("[Enter Exception]", e, flush=True)
            # pass 
        except exceptions.NoSuchElementException as e:
            print("[No_Such_Element Exception]", e, flush=True)
        finally:
            attempts -= 1

    if attempts == 0:
        print("[Warning]: Attempts exceeded")
