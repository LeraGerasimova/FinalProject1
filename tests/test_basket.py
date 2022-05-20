from pages.basket_page import BasketPage


#1 Проверка добавления книги в корзину
def test_add_book_in_basket(web_browser):
    page = BasketPage(web_browser)
    page.Editor_choice.click()
    page.In_basket.click()
    page.basket.click()
    assert page.order_availability

#2 Проверка увеличения книги на 1
def test_add_two_books_in_basket(web_browser):
    page = BasketPage(web_browser)
    page.Editor_choice.click()
    page.In_basket.click()
    page.basket.click()
    page.plus.click()
    assert page.two_books_in_basket

#3 Проверка очистки корзины
def test_delete_books_in_basket(web_browser):
    page = BasketPage(web_browser)
    page.Editor_choice.click()
    page.In_basket.click()
    page.basket.click()
    page.clear_basket.click()
    assert page.empty_basket

#4 Проверка восстановления удаленных товаров
def test_restore_product(web_browser):
    page = BasketPage(web_browser)
    page.Editor_choice.click()
    page.In_basket.click()
    page.basket.click()
    page.clear_basket.click()
    page.restore_product.click()
    assert page.order_availability

#5 Проверка кнопки как сделать заказ
def test_how_to_place_order(web_browser):
    page = BasketPage(web_browser)
    page.basket.click()
    page.how_to_place_order.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?cardhelp=192'

#6 Проверка кнопки как получить заказ
def test_how_to_get_order(web_browser):
    page = BasketPage(web_browser)
    page.basket.click()
    page.how_to_get_order.click()
    assert page.get_current_url() == 'https://www.labirint.ru/delivery/'

#7 Проверка кнопки как можно оплатить его
def test_how_can_pay_it(web_browser):
    page = BasketPage(web_browser)
    page.basket.click()
    page.how_can_pay_it.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?cardhelp=81'






















