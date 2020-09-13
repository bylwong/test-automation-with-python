from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)
driver.set_window_size(1024, 800)
driver.get("https://www.demoblaze.com/")

login_button = driver.find_element_by_id("login2")
login_button.click()

sleep(1)
login_modal = driver.find_element_by_id("logInModal")
username_input = login_modal.find_element_by_id("loginusername")
username_input.clear()
username_input.send_keys("a")

password_input = login_modal.find_element_by_id("loginpassword")
password_input.clear()
password_input.send_keys("a")

login_submit = login_modal.find_element_by_class_name("btn-primary")
login_submit.click()

products_table = driver.find_element_by_id("tbodyid")
cards = products_table.find_elements_by_class_name("card-title")  # returns a list

for card in cards:
    print(card.text)

sleep(5)
driver.quit()
