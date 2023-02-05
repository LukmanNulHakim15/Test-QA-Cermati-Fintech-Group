from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=options)
browser = driver.get("https://www.cermati.com/app/gabung")

time.sleep(3)
trial = driver.find_element('id', 'email') 
trial.send_keys("lukmannul1515@gmail.com")
assert trial == trial, "Failed"
print("passed")

time.sleep(3)
trial2 = driver.find_element('id','mobilePhone')
trial2.send_keys("0895330163328")
assert trial2 == trial2, 'failed input mobile phone'
print('passed')

time.sleep(3)
trial3 = driver.find_element('id','password')
trial3.send_keys('Lukman123')
assert trial3 == trial3, 'failed input password'
print('passed')

time.sleep(3)
trial4 = driver.find_element('id', 'confirmPassword')
trial4.send_keys('Lukman123')
assert trial4 == trial4, 'failed input confirm password'
print('passed')

time.sleep(3)
trial5 = driver.find_element('id', 'firstName')
trial5.send_keys('Lukman')
assert trial5 == trial5, 'failed input first name'
print('passed')

time.sleep(3)
trial6 = driver.find_element('id','lastName')
trial6.send_keys('Hakim')
assert trial6 == trial6, 'failed input last name'
print('passed')

time.sleep(3)
trial7 = driver.find_element('id', 'cityAndProvince').click()
time.sleep(3)
pyautogui.typewrite('KABUPATEN LEBAK')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

driver.find_element(By.XPATH,"/html//div[@id='safe-area']//div[@class='container_Eq-qi']/button[@type='button']").click()
print('passed submit')
time.sleep(3)
