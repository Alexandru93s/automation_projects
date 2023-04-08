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
cautare_rtx.send_keys("RTX 3060 TI" + Keys.ENTER)
driver.implicitly_wait(5)
compari = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/a/h3")
compari.click()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, 'dismiss').click()  #got an error:element is not clickable at point beacuse another element obscures it.Workaround needed
vision_oc = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[1]/h2/a')
vision_oc.click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/div/div[1]/div[3]/div[1]/div[1]/div[7]/div[1]').click()
driver.implicitly_wait(15)
