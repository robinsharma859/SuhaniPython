import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    
       def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30);

        
        
       def Click_HeaderTab(self, tab_name):
        try:
            print(f"Attempting to click on header tab: {tab_name}")
            headertab =f"//div[@id='navbarExample']//li/a[text()='{tab_name}']";
            print(f"Header tab XPath: {headertab}")
            header_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, headertab)))
            header_tab.click();
            print(f"Clicked on header tab: {tab_name}")
        except Exception as e:
            print(f"Error clicking on header tab '{tab_name}': {str(e)}")
        
       def ValidateLinkIsAvailable(self,tab_name):
        try:
            headertab =f"//div[@id='navbarExample']//li/a[text()='{tab_name}']";
            print(f"Header tab XPath: {headertab}")
            header_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, headertab)))
            is_displayed =  header_tab.is_enabled()
            print(is_displayed);
            return is_displayed;

        except Exception as e:
            print(f"Error occured while validating visible property for '{tab_name} : {str(e)}");
            return False
       
       def Select_Category(self,categoryName):
        try:
          category =f"//a[@id='itemc' and contains(normalize-space(.), '{categoryName}')]";
          category = self.wait.until(EC.element_to_be_clickable((By.XPATH, category)))
          category.click();
          time.sleep(3);
          print(f"Category '{categoryName}' is clicked sucessfully");

        except Exception as e:
          print("Eror occured while selecting Category"); 
        
       def Select_Product(self,productName):
        try:
             product = f"//a[text()='{productName}']";
             product =  self.wait.until(EC.element_to_be_clickable((By.XPATH, product)))
             product.click();
             time.sleep(3);
             print(f"Product '{productName}' is clicked sucessfully");
        except Exception as e:
         print(f"Error occured while selecting productName '{productName}' : : {str(e)} ")
         
       def Add_Product_Cart(self):
        try:
         product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
         product.click();
         time.sleep(1);
         print("Waiting for alert to appear...")
         alert = self.driver.switch_to.alert
         message = alert.text
         alert.accept()
         print(f"Alert messge is  '{message}'")
         return message;
        except Exception as e:
            print(f"error occured while adding product to cart : {str(e)}")
            
        
         
        
            
              
        
      
                
            
     