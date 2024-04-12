from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_item_to_the_basket()
    page.solve_quiz_get_code()
    page.book_name()
    page.items_in_basket()
    page.item_price_and_total_price_are_the_same()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_item_to_the_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_item_to_the_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.items_in_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_items_in_the_basket()
    basket_page.your_basket_is_empty_text()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = "1231231241515"
        login_page = LoginPage(browser, self.link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.items_in_basket()
        basket_page = BasketPage(browser, self.link)
        basket_page.should_be_no_items_in_the_basket()
        basket_page.your_basket_is_empty_text()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_add_item_to_the_basket()
        page.solve_quiz_get_code()
        page.book_name()
        page.items_in_basket()
        page.item_price_and_total_price_are_the_same()
