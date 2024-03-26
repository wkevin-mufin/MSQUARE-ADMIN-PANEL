from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Enter username
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input_login_email"))
        )
        username_field.send_keys(username)

        # Enter password
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input_login_password"))
        )
        password_field.send_keys(password)

        # Click login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_login_sign_in"))
        )
        login_button.click()

        # Wait for login to complete (you may need to adjust the conditions)
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )
