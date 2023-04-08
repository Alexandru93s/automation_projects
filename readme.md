
# Selenium WebDriver

This is where I keep some notes for Selenium WebDriver automation testing.

# To make Chrome work without closing immediatly






```sh
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.chrome.options import Options
  from webdriver_manager.chrome import ChromeDriverManager
  options = Options()
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
```
 
 
 ![Firefoxgif](https://github.com/Alexandru9s/automation_projects/blob/master/seleniumautomationvideo.gif)
