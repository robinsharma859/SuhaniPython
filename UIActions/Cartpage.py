import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cartpage:
    
  usernamebyId = "name";
  countryId="country"
  cityId = "city"
  creditId = "card";
  orderId = "//p[@class='lead text-muted ']"
  
  def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30);
        
  def clickOrderButton(self):
     try:
        order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        order_button.click();
        print("Order button is clicked");
     except Exception as e:
      print("Error occured while clicking order button")
      
  def PlaceOrder(self,name,country,city,creditCard):
    try:
     self.usernamebyId = self.wait.until(EC.element_to_be_clickable((By.ID, self.usernamebyId)));
     self.countryId = self.wait.until(EC.element_to_be_clickable((By.ID, self.countryId)));
     self.cityId = self.wait.until(EC.element_to_be_clickable((By.ID, self.cityId)));
     self.creditId = self.wait.until(EC.element_to_be_clickable((By.ID, self.creditId)));
     
     self.usernamebyId.send_keys(name)
     self.countryId.send_keys(country),
     self.cityId.send_keys(city)
     self.creditId.send_keys(creditCard);
     
     print("Order required details are submitted");
     purchase_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Purchase']")));
     purchase_Button.click();
     time.sleep(2);
     orderDetails = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.orderId)));
     result = orderDetails.text
     print(result);
    except Exception as e:
     print(f"Error occured while making order '{str(e)}'")