import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
from Browser import Browser
from UIActions.HomePage import HomePage
from Enums import HeaderLink
from UIActions.SignUp import SignUp
from UIActions.Login import LoginUI
from UIActions.Cartpage import Cartpage



class TestClass:

   @pytest.fixture(autouse=True)
   def setup(self):
        self.browser = Browser()
        self.driver = self.browser.get_driver()
        yield

        if self.driver:
            self.driver.quit()
    
   def test_ValidatUserCan_SignUp(self):
        print("Starting test: test_ValidatUserCan_SignUp")
        home_page = HomePage(self.driver)
        home_page.Click_HeaderTab(HeaderLink.SIGN_UP.value)
        print("User can click on Sign up tab successfully")
        SignUpPage = SignUp(self.driver)
        username = f"SuhaniUser{random.randint(1000, 9999)}"
        message = SignUpPage.sign_up(username, "124");
        assert message == "Sign up successful.", f"Expected 'Sign up successful.', but got '{message}'"
        
   def test_Login_Functionality(self):
        print("Starting test: Login Test case")
        home_page = HomePage(self.driver)
        home_page.Click_HeaderTab(HeaderLink.LOG_IN.value)
        print("User can click on Login  tab successfully")
        Login = LoginUI(self.driver)
        Login.Loging_IntoApplication("suhani111214", "124");
        result = home_page.ValidateLinkIsAvailable("Log out");
        print(f"log out button is '{result}'");
        assert result == True, f"Expected 'Login is successful.'"
  
   def test_Login_FunctionalityInvalidRecord(self):
        print("Starting test: Login Test case")
        home_page = HomePage(self.driver)
        home_page.Click_HeaderTab(HeaderLink.LOG_IN.value)
        print("User can click on Login  tab successfully")
        Login = LoginUI(self.driver)
        Login.Loging_IntoApplication("suhani111214", "1214");
        message = Login.GetAlert_Message()
        assert message == "Wrong password.", f"Expected 'Login is successful.', but got '{message}'"
        
   def test_userSelectProduct_AddCart(self):
        home_page = HomePage(self.driver)
        home_page.Select_Category("Laptop")
        home_page.Select_Product("Sony vaio i5");
        message = home_page.Add_Product_Cart();
        assert message == "Product added", f"Expected Product added message but got  '{message}'"

   def test_OrderProcess(self):
       print("Excecuting test case for making order")
       home_page = HomePage(self.driver)
       home_page.Select_Category("Laptop")
       home_page.Select_Product("Sony vaio i5");
       home_page.Add_Product_Cart();
       cart_page = Cartpage(self.driver);
       home_page.Click_HeaderTab("Cart");
       cart_page.clickOrderButton();
       cart_page.PlaceOrder("Suhani Aagarwal","India","Noida","1234-12344");
        
        
        
            
            