from enum import Enum


class HeaderLink(Enum):
    HOME = "Home"
    CONTACT = "Contact"
    CART = "Cart"
    LOG_IN = "Log in"
    SIGN_UP = "Sign up"


class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"