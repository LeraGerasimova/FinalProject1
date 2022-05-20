import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class Search(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.labirint.ru/"
        super().__init__(web_driver, url)

    # Локаторы
    #cтрока поиска
    search_panel = WebElement(css_selector = ".b-header-b-search-e-input")
    # кнопка поиска
    search_button = WebElement(css_selector = ".b-header-b-search-e-srch-icon")
    # название книги
    products_titles = ManyWebElements(css_selector = ".product-title-link")
    #
    title = WebElement(css_selector = "h1")






