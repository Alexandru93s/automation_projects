from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.google.com')
driver.implicitly_wait(5)
respinge_tot = driver.find_element(By.ID,'W0wltc')         #reject all cookie settings
respinge_tot.click()                                        
driver.implicitly_wait(3)
cautare_rtx = driver.find_element(By.NAME, 'q')
cautare_rtx.click()
cautare_rtx.send_keys("RTX 3060 TI" + Keys.ENTER)           #search for GPU on google
driver.implicitly_wait(5)
compari = driver.find_element(By.PARTIAL_LINK_TEXT, "Compari.ro")   #go to compari
compari.click()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, 'dismiss').click()  #got an error:element is not clickable at point beacuse another element obscures it.Workaround needed
vision_oc = driver.find_element(By.PARTIAL_LINK_TEXT, 'GIGABYTE GeForce RTX 3060 Ti VISION OC')
vision_oc.click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, 'fjump').click()
driver.implicitly_wait(15)
