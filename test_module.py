from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)
driver.set_window_size(1024, 800)
driver.get("https://www.demoblaze.com/")

login_button = driver.find_element_by_id("login2")
login_button.click()

sleep(5)
driver.quit()
