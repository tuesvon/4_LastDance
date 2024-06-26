from .base_page import BasePage
from .locators import AddBooktotheBasket
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def should_add_item_to_the_basket(self):
        assert self.browser.find_element(*AddBooktotheBasket.ADDBOOK), "Нет кнопки для добавления товара"
        add_item = self.browser.find_element(*AddBooktotheBasket.ADDBOOK)
        add_item.click()

    def book_name(self):
        book_name = self.browser.find_element(*AddBooktotheBasket.BOOKNAME)
        success_message = self.browser.find_element(*AddBooktotheBasket.SUCCESSMESSAGE)
        assert book_name.text == success_message.text, \
            f"Выбрана не та книга. Имя книги: {book_name.text}, а в сообщении указано: {success_message.text}"

    def items_in_basket(self):
        assert self.browser.find_element(*AddBooktotheBasket.ITEMSINBASKET), "Нет кнопки просмотра корзины"
        gotobasketbtn = self.browser.find_element(*AddBooktotheBasket.ITEMSINBASKET)
        gotobasketbtn.click()

    def item_price_and_total_price_are_the_same(self):
        book_price = self.browser.find_element(*AddBooktotheBasket.BOOKPRICE)
        total_price = self.browser.find_element(*AddBooktotheBasket.TOTALBASKETPRICE)
        assert book_price.text == total_price.text, \
            f"Что-то пошло не так. Цена одной книги: {book_price.text}, а общая сумма: {total_price.text}"

    def is_not_element_present(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(AddBooktotheBasket.SUCCESSMESSAGE)
            )
        except TimeoutException:
            return True
        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(), "Сообщение отображается, хотя не должно"

    def is_disappeared(self, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout,1, TimeoutException).
             until_not(EC.presence_of_element_located(AddBooktotheBasket.SUCCESSMESSAGE)))
        except TimeoutException:
            return False
        return True

    def success_message_should_disappear(self):
        assert self.is_disappeared(), "Сообщение отображается"
