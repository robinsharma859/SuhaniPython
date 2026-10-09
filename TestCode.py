import random

from Browser import Browser
from Enums import HeaderLink
from UIActions.SignUp import SignUp
from UIActions.HomePage import HomePage
from UIActions.Login import LoginUI
from UIActions.Cartpage import Cartpage



class TestCode:

    def __init__(self):
        self.browser = Browser()
        self.driver = self.browser.get_driver()

    def TestMe(self):
        home_page = HomePage(self.driver)
        home_page.Select_Category("Laptop")
        home_page.Select_Product("Sony vaio i5");
        home_page.Add_Product_Cart();
        cart_page = Cartpage(self.driver);
        home_page.Click_HeaderTab("Cart");
        cart_page.clickOrderButton();
        cart_page.PlaceOrder("Suhani Aagarwal","India","Noida","1234-12344");
        
    def TestRandom(self):
        username = f"SuahniUser{random.randint(1000, 9999)}"
        print(username)
    
        
       


testcode = TestCode()
testcode.TestRandom()