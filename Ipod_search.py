from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()
driver.maximize_window()
#Wait for later use
wait = WebDriverWait(driver, 20)
#Go to google.com
driver.get('https://google.com')
#Wait until cookie button appears
wait.until(EC.element_to_be_clickable((By.ID, 'W0wltc')))
#Reject cookies
reject_cookies = driver.find_element(By.ID, 'W0wltc')
reject_cookies.click()
#Search google for PC Garage
search_site = driver.find_element(By.NAME, 'q')
search_site.click()
search_site.send_keys('OLX')
search_site.send_keys(Keys.ENTER)
#Go to site
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'OLX')))
site = driver.find_element(By.PARTIAL_LINK_TEXT, 'OLX')
site.click()
#Accept cookies
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id = "onetrust-accept-btn-handler"]')))
accept_cookies = driver.find_element(By.CSS_SELECTOR, 'button[id = "onetrust-accept-btn-handler"]')
accept_cookies.click()
#Search for Ipod Classic
wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="onetrust-pc-dark-filter ot-fade-in"]')))
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="headerSearch"]')))
ipod_search = driver.find_element(By.XPATH, '//input[@id="headerSearch"]')
ipod_search.click()
ipod_search.send_keys('Ipod Classic')
ipod_search.send_keys(Keys.ENTER)
#Sort prices in ascending order
#Get all prices below the price I set
#Add them to an excel sheet
