from selenium import webdriver

from GlobalParamaters import BASE_URL, BROWSER, Global_Wait


class Browser:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = None

    def get_driver(self):
        if self.driver is not None:
            return self.driver

        try:
            print("Initializing the driver for browser: ", BROWSER)
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.implicitly_wait(Global_Wait)
            self.driver.get(BASE_URL)
            print("Driver is initialized successfully")
            return self.driver
        except Exception as e:
            print("Error initializing the driver: ", str(e))
            self.driver = None
            return None

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None