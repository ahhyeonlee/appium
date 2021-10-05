from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, requests, sys
import mail as m
import drivers as d 
import settings as s

global results, driver

def run(device_id) :
    results = []
    desired_caps = s.setting(device_id)
    driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.switch_to.context('NATIVE_APP')
    appium(results, driver, desired_caps['app_name'])
    driver.quit()
    m.mail(results)

def appium(results, driver, app_name):
    scenarioList = requests.get("http://localhost:8080/get/scenario/" + app_name).json()
    for scenario in scenarioList : 
        scenario_id = scenario['id']
        case_result = []
        cases = requests.get("http://localhost:8080/get/case/" + scenario_id).json()
        for case in cases : 
            if case['gubun'] == "click" : 
                chk = d.findElementByID(driver, case['element_id'])
            elif case['gubun'] == "xpath" : 
                chk = d.findElementByXPath(driver, case['element_id'])
            elif case['gubun'] == "input":
                chk = d.findElementByInput(driver, case['element_id'], case['element_value'])
            else :
                chk = d.driverBack(driver)

            if case['gubun'] != "back" and chk is True:
                temp = [case['element_id'], "성공"]
                case_result.append(temp)
            elif case['gubun'] == "back" and chk is True : 
                temp = ["driver.back()", "성공"]
                case_result.append(temp)                
            else : 
                temp = [case['element_id'], "실패"]
                case_result.append(temp)
        results.append([scenario['title'], case_result])

if __name__ == "__main__":
    # execute only if run as a script
    run("c30415b70999406ca2e478c38fa5ebec")