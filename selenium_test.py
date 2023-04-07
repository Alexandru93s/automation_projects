from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('https://www.google.com')
driver.implicitly_wait(5)
respinge_tot = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div')         #reject all cookie settings
respinge_tot.click()
driver.implicitly_wait(3)
cautare_rtx = driver.find_element(By.NAME, 'q')
cautare_rtx.send_keys('RTX 3060 TI' + Keys.ENTER)           #search for gpu
driver.implicitly_wait(2)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/a/h3').click()      #go to compari
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div[10]/div[1]/div[1]/div[1]').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[1]/div[3]/div[1]/div[1]/div[7]/div[1]').click()
driver.implicitly_wait(10)
accept_cookies = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div[2]')
accept_cookies.click()