from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REG_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    SIGN_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class AddBooktotheBasket():
    ADDBOOK = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOKNAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    SUCCESSMESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOKPRICE = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-1 > p")
    ITEMSINBASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > "
                                      "div.basket-mini.pull-right.hidden-xs > span > a")
    TOTALBASKETPRICE = (By.CSS_SELECTOR, "#basket_formset > div > div > div:nth-child(5) > p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
