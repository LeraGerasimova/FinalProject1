import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class BodyPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.labirint.ru/"
        super().__init__(web_driver, url)

    # Локаторы
    # Лучшая покупка дня
    best_buy_day = WebElement(css_selector = "[href='/best/sale/']")
    #количество книг на странице лучшая покупка дня
    number_of_books = ManyWebElements(css_selector = ".products-row-outer")
    #заглавие страницы Главные книги 2022
    title_page = WebElement(css_selector = "h1")
    # Что почитать: выбор редакции
    editor_choice = WebElement(css_selector="[href='/top/toread/']")
    # Больше книг со скидками
    more_books_with_discounts = WebElement(css_selector= ".btn-not-avaliable")
    #Библионочь 2022
    biblionoch  = WebElement(css_selector= "[href='/biblionight/']")
    #Нужные учебники для вас в этом году
    right_textbooks_button = WebElement(xpath='//a[@class="block-link-title" and contains(text(),"Нужные учебники для вас в этом году")]')
    # Читатели выбирают сегодня
    readers_choice = WebElement(css_selector= "[href='/best/']")
    #Лабиринт. Сейчас
    labirint_now = WebElement(css_selector= "[href='/now/']")
    # Лабиринт. Сейчас строка меню
    labirint_now_menu_bar = WebElement(css_selector= ".mm-link-big-m-sub")
    # Детский навигатор — что читать детям и с детьми
    children_navigator = WebElement(css_selector= ".block-link-title[href='/child-now/']")
    # детский навигатор строка меню
    children_navigator_menu_bar = WebElement(css_selector= "[href='/child-now/']")
    # книжные лидеры продаж
    book_sales_leader = WebElement(css_selector= "[href='/rating/?period=2&id_genre=1852']")
    # Книги:новинки 2022
    books_new_items_2022 = WebElement(css_selector= "[href='/novelty/']")
    #Книжные обзоры и рецензии
    book_reviews_and_reviews = WebElement(css_selector= "[href='/news/books/']")
    # Книжные обзоры и рецензии строка меню
    book_reviews_and_reviews_menu_bar = WebElement(css_selector = ".ratingh")
    # количество книг на странице Книжные обзоры и рецензии
    number_of_books_reviews = ManyWebElements(css_selector = ".bl-right-main")
    #Нас ценят
    we_are_appreciated = WebElement(css_selector = "[data-event-label='openReviewYM']")
    #Правила
    rules = WebElement(css_selector = "[href='/help/?cardhelp=2300']")










