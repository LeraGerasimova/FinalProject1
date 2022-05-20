from pages.search import Search

#1 проверка позитивного вводв в поиск
def test_search(web_browser):
    page = Search(web_browser)
    page.search_panel = 'school'
    page.search_button.click()
    assert page.products_titles.count() == 60

#2 проверка поиска при вводе символов *%:;"
def test_checking_characters(web_browser):
    page = Search(web_browser)
    page.search_panel = '*%:;"'
    page.search_button.click()
    assert page.products_titles.count() == 0
    assert page.title.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"



