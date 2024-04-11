from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_be_no_items_in_the_basket(self):
        try:
            self.browser.find_element(*BasketPageLocators.NO_ITEMS_IN_THE_BASKET)
        except NoSuchElementException:
            return False
        return True

    def your_basket_is_empty_text(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert empty_basket.text is not None, "В корзине что-то лежит"
