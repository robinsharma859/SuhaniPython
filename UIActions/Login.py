import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginUI:

    userNameById = "loginusername"
    passwordById = "loginpassword"
    loginButtonXpath = "//button[normalize-space()='Log in']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def __enter_username(self, username):
        try:
            username_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.userNameById)))
            username_field.clear()
            username_field.send_keys(username)
            print(f"Entered username: {username}")
        except Exception as e:
            print(f"Error entering username: {str(e)}")

    def __enter_password(self, password):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.passwordById)))
            password_field.clear()
            password_field.send_keys(password)
            print(f"Entered password: {password}")
        except Exception as e:
            print(f"Error entering password: {str(e)}")

    def __click_login_button(self):
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.loginButtonXpath)))
            login_button.click()
            print("Clicked on Login  button")
        except Exception as e:
            print(f"Error clicking on Login button: {str(e)}")

    def Loging_IntoApplication(self, username, password):
        try:
            self.__enter_username(username)
            self.__enter_password(password)
            time.sleep(2)

            self.__click_login_button()
            print("Waiting for Logut button to appear...")
            time.sleep(6)
          
        except Exception as e:
            print(f"Error during sign up process: {str(e)}")

    def get_userName(self):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.userNameById)))
        return username_field
    
    def GetAlert_Message(self):
        try:
            print("Waiting for alert to appear...")
            time.sleep(2)
            alert = self.driver.switch_to.alert
            message = alert.text
            alert.accept()
            time.sleep(2)
            print(f"Alert messge is  '{message}'")
            return message;
             
        except Exception as e:
             print(f"Error during Getting alert message: {str(e)}")
             return None