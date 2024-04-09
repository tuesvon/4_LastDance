from .base_page import BasePage
from .locators import AddBooktotheBasket


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
        book_price = self.browser.find_element(*AddBooktotheBasket.TOTALBASKETPRICE)
        total_price = self.browser.find_element(*AddBooktotheBasket.TOTALBASKETPRICE)
        assert book_price.text == total_price.text, \
            f"Что-то пошло не так. Цена одной книги: {book_price.text}, а общая сумма: {total_price.text}"

