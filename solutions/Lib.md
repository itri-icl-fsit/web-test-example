# Usage

## Stale Element Function

### Main Function

- def repeat_action(action, driver, dict_arg, attempts)
  - ``action``: a function which do some sequence action (Function)
  - ``driver``: Selenium Webdriver
  - ``dict_arg``: if your function need argument, you can write in this dictionary (Dictionary), default is ``{}``
  - ``attempts``: retry times (Integer), default is ``5``
  - Returns: NULL

Example 1: 

```python
repeat_action(custom_action, chrome_driver, {'my_key': '#my_btn_id'}, 5)
# The name of key can be changed by yourself. 
# You must read the corresponding key_value in your custom function.

# For example:
def custom_action(driver, dictionary):
    # read argument with key
    btn = driver.find_element_by_css_selector(dictionary['my_key'])   
```

Example 2: 
```python
def custom_action(driver):
    # if your function doesn't need parameter
    btn = driver.find_element_by_css_selector('#target_id')  

# then you can pass a empty dictionary into repeat_action()
repeat_action(custom_action, driver, {}, 5)
```

### Other function

- def click_action(driver, dict_arg):
  - ``driver``: Selenium Webdriver
  - ``dict_arg``: Parameter, need contain ``click`` key and its corresponding value is the css_selector of target.
  - Usually, we call it with ``repeat_action`` action, we just need to indicate the css_selector.
  - Example:
    ```python
    repeat_action(click_action, driver, {'click': '#target_id'}, 5)
    ```

**There are some similar function** :

- def checkbox_action(driver, dict_arg):
  - ``driver``: Selenium Webdriver
  - ``dict_arg``: Parameter, need contain  ``checkbox`` key 
  - Example:
    ```python
    repeat_action(checkbox_action, driver, {'checkbox': '#target_id'}, 5)
    ```

- def sendkeys_action(driver, dict_arg):
  - ``driver``: Selenium Webdriver
  - ``dict_arg``: Parameter, need contain  ``sendkeys`` key (target id) and ``text`` key (typed-in words).
  - Example:
    ```python
    repeat_action(sendkeys_action, driver, {'sendkeys': '#target_id', 'text': 'words_you_want_to_type_in'}, 5)
    ```

    
## Hidden Element Issue Related Function

- def click_hidden_by_selector(driver, dict_arg):
  - It's a special function for **hidden element issue**, implemented for those covered element.
  
    - You can use some "combo" like ``custom_action`` with this function !
    - Principle: Use JS function to make web execute.
  
  - ``driver``: Selenium Webdriver
  
  - ``dict_arg``: Parameter, need contain ``click`` key and its corresponding value is the css_selector of target.
  
  - Example: 
  
    ```python
    click_hidden_by_selector(driver, {'click': '#target_id'})
    ```
- def click_hidden_by_xpath(driver, dict_arg):
  - It's the xpath version, compared to css_selector version.
  
  - ``driver``: Selenium Webdriver
  
  - ``dict_arg``: Parameter, need contain ``click`` key and its corresponding value is the xpath of target.
  
  - Example: 
  
    ```python
    click_hidden_by_xpath(driver, {'click': "//select/option[text()='Click Me!']"})
    ```

# Feature

- If stale exception occurred, terminal will show message.
  - Therefore, if there is no relevant message printed, it means Stale Issue isn't triggered.
  - ![](https://i.imgur.com/1bXJK9F.png)

- If you call a build-in function with wrong argument, it will display some information.
  - ![](https://i.imgur.com/7OImiJC.png)



# Troubleshooting

## Dictionary KeyError

Example : 

![](https://i.imgur.com/7OImiJC.png)

- This is because for some function, parameter are pre-set.
    ![](https://i.imgur.com/51bBoq4.png)

## No_Such_Element Exception
Example : 

![](https://i.imgur.com/Sj6mLf0.png)

- This means seleinum can't catch element with your css selector.
  Sometimes, this is a variant of the stale element problem.
  So I still let program try to catch element again.
  If this message is printed to the end, please check your css selector is correct or increase the ``attempts`` parameter.

![](https://i.imgur.com/AFJ7QxY.png)

