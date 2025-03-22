from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Ensure this path is correct
chrome_driver_path = r"C:\Users\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()
