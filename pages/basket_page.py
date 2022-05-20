import os
from pages.base import WebPage
from pages.elements import WebElement

class BasketPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.labirint.ru/"
        super().__init__(web_driver, url)

    # Локаторы
    #Что почитать: выбор редакции
    Editor_choice = WebElement(css_selector = "[href='/top/toread/']")
    #кнопка В корзину под книгой правило 5 секунд
    In_basket = WebElement(css_selector = "[data-carttext='']")
    #корзина
    basket = WebElement(xpath='//span[@class="b-header-b-personal-e-text" and contains(text(),"Корзина")]')
    #ваш заказ
    order_availability = WebElement(css_selector = ".g-alttext-small")
    # значок +
    plus = WebElement(css_selector = ".btn-increase-cart")
    # увеличение книги на одну
    two_books_in_basket = WebElement(css_selector = ".quantity")
    # кнопка очистить корзину
    clear_basket = WebElement(css_selector = ".b-link-popup")
    # ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?
    empty_basket = WebElement(css_selector = ".g-alttext-grey")
    # кнопка восстановить удаленное
    restore_product = WebElement(css_selector = ".b-link-popup")
    # как сделать заказ
    how_to_place_order = WebElement(css_selector = "[href='/help/?cardhelp=192']")
    # как получить заказ
    how_to_get_order = WebElement(css_selector = "[href='/delivery/']")
    # как можно оплатить его
    how_can_pay_it = WebElement(css_selector = "[href='/help/?cardhelp=81']")







