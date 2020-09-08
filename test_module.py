from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)
driver.get("https://www.demoblaze.com/")

sleep(5)
driver.quit()
