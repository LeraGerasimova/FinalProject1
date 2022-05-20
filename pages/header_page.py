import os
from pages.base import WebPage
from pages.elements import WebElement

class HeaderPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.labirint.ru/"
        super().__init__(web_driver, url)


    #Locators

    #окно авторизации
    login = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    #кнопка логотипа
    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    #кнопка Сообщения
    messages = WebElement(xpath='//span[@class="b-header-b-personal-e-text" and contains(text(),"Сообщения")]')
    #Мой Лабиринт
    My_lab = WebElement(xpath='//*[@class="js-b-autofade-text"]')
    #кнопка Отложено
    postponed = WebElement(xpath='//span[@class="b-header-b-personal-e-text" and contains(text(),"Отложено")]')
    #кнопка Корзина
    basket = WebElement(xpath='//span[@class="b-header-b-personal-e-text" and contains(text(),"Корзина")]')
    #скидки сегодня
    discounts_today = WebElement(xpath='//span[@class="itm-md-vis-hdn itm-lg-vis-shw"]')
    #кнопка Книги
    books = WebElement(xpath='//span[@class="b-header-b-menu-e-link top-link-menu first-child"]')
    #кнопка Главное 2022
    Main = WebElement(xpath='//li[@class="b-header-b-menu-e-list-item analytics-click-js"]')
    #кнопка Школа
    School = WebElement(css_selector = ".b-header-b-menu-e-link [href='/school/']")
    #кнопка Игрушки
    Toys = WebElement(css_selector = "[href='/games/']")
    #кнопка Канцтовары
    Stationery = WebElement(css_selector = "[href='/office/']")
    # кнопка Клуб
    Club = WebElement(css_selector = "[href='/club/']")
    # кнопка Доставка и оплата
    Delivery_and_payment = WebElement(css_selector = "[href = '/help/']")
    # кнопка Сертификаты
    Certificates = WebElement(css_selector = "[href='/top/certificates/']")
    # кнопка Рейтинги
    Ratings = WebElement(css_selector = "[href='/rating/?id_genre=-1&nrd=1']")
    # кнопка Новинки
    New_products = WebElement(css_selector = "[href='/novelty/']")
    # кнопка Скидки
    Discounts = WebElement(css_selector = "[href='/sale/']")
    # кнопка Контакты
    Contacts = WebElement(css_selector = ".b-header-b-sec-menu-e-link[href='/contact/']")
    # кнопка Поддержка
    Support = WebElement(css_selector = "[href='/support/']")
    # кнопка 554 пункта самовывоза
    PickupPoint = WebElement(css_selector = "[href='/maps/']")










