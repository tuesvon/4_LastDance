from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REG_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    SIGN_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


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
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > "
                                        "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    NO_ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR, "#content_inner > div.form-group.clearfix > div > div > a")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
