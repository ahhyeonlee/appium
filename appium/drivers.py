from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def driverBack(driver): 
    try : 
        driver.back()
        return True
    except Exception as e:
        print(e)
        return False

def findElementByID(driver, input):
    try:
        driver.find_element_by_id(input).click()
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False

def findElementByXPath(driver, input):
    try:
        driver.find_element_by_id(input).click()
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False

def findElementByInput(driver, element, input):
    try:
        driver.find_element_by_id(element).send_keys(input)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False
