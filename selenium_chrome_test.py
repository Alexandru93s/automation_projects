from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://www.google.com")
respinge_tot = driver.find_element(By.ID, "W0wltc")
respinge_tot.click()
cautare = driver.find_element(By.NAME, "q")
cautare.send_keys("RTX 3070" + Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a').click()

