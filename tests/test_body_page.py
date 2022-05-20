import pytest

from pages.body_page import BodyPage


#1 Проверка перехода в Лучшая покупка дня
def test_best_buy_day(web_browser):
    page = BodyPage(web_browser)
    page.best_buy_day.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'главные книги 2022' in title.lower()

#2 Проверка перехода в Что почитать? выбор редакции
def test_what_to_read_editors_choice(web_browser):
    page = BodyPage(web_browser)
    page.editor_choice.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/toread/'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'что почитать: выбор редакции' in title.lower()

#3 Переход в Больше книг со скидками
def test_more_books_with_discounts(web_browser):
    page = BodyPage(web_browser)
    page.more_books_with_discounts.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'главные книги 2022' in title.lower()

#4 Переход в Библионочь 2022
def test_biblionoch_click(web_browser):
    page = BodyPage(web_browser)
    page.biblionoch.click()
    assert page.get_current_url() == 'https://www.labirint.ru/biblionight/'

#5 Переход в Нужные учебники для вас в этом году БАГ
""""При проверке теста элемент не найден, на сайте элемент присутствует"""
@pytest.mark.xfail(reason = 'Element not visible')
def test_right_textbooks(web_browser):
    page = BodyPage(web_browser)
    page.right_textbooks_button.wait_until_not_visible()
    assert page.get_current_url() == 'https://www.labirint.ru/biblionight/'

#6  Переход в Читатели выбирают сегодня
def test_readers_choice(web_browser):
    page = BodyPage(web_browser)
    page.readers_choice.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'главные книги 2022' in title.lower()

#7 Переход в Лабиринт. Сейчас книжные события мая
def test_labirint_now(web_browser):
    page = BodyPage(web_browser)
    page.labirint_now.click()
    assert page.get_current_url() == 'https://www.labirint.ru/now/'
    title = page.labirint_now_menu_bar.get_text()
    assert 'лабиринт. сейчас' in title.lower()


#8 проверка перехода в Детский навигатор — что читать детям и с детьми
def test_children_navigator(web_browser):
    page = BodyPage(web_browser)
    page.children_navigator.click()
    assert page.get_current_url() == 'https://www.labirint.ru/child-now/'
    title = page.children_navigator_menu_bar.get_text()
    assert 'детский навигатор' in title.lower()

#9 проверка перехода в книжные лидеры продаж
def test_book_sales_leader(web_browser):
    page = BodyPage(web_browser)
    page.book_sales_leader.click()
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?period=2&id_genre=1852'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'художественная литература. рейтинг продаж' in title.lower()

#10 проверка перехода в Книги: новинки 2022
def test_books_new_items_2022(web_browser):
    page = BodyPage(web_browser)
    page.books_new_items_2022.click()
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'
    assert page.number_of_books.count() >= 1
    title = page.title_page.get_text()
    assert 'новые книги' in title.lower()

#11 проверка перехода в Книжные обзоры и рецензии
def test_book_reviews_and_reviews(web_browser):
    page = BodyPage(web_browser)
    page.book_reviews_and_reviews.click()
    assert page.get_current_url() == 'https://www.labirint.ru/news/books/'
    assert page.number_of_books_reviews.count() >= 1
    title = page.book_reviews_and_reviews_menu_bar.get_text()
    assert 'книжные обзоры и рецензии' in title.lower()

#12 проверка перехода в Нас ценят!
""""При проверке теста элемент не найден, на сайте элемент присутствует"""
@pytest.mark.xfail(reason = 'Element not visible')
def test_we_are_appreciated(web_browser):
    page = BodyPage(web_browser)
    page.we_are_appreciated.wait_until_not_visible()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://market.yandex.ru/shop--labirint/1550/reviews?grade_value=5&sort_by=date'

#13 проверка перехода в Правила в разделе Вам подарок
def test_rules(web_browser):
    page = BodyPage(web_browser)
    page.rules.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?cardhelp=2300'
    title = page.title_page.get_text()
    assert 'купон' in title.lower()













































