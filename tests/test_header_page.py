from selenium.webdriver import ActionChains
from pages.header_page import HeaderPage

#1 клик по логотипу Лабиринт
def test_logo_click(web_browser):
    page = HeaderPage(web_browser)
    page.logo.click()
    assert page.get_current_url() == 'https://www.labirint.ru/'

#2 переход в Сообщения
def test_message_click(web_browser):
    page = HeaderPage(web_browser)
    page.messages.click()
    assert page.login

#3 Переход в Мой Лабиринт
def test_my_lab_click(web_browser):
    page = HeaderPage(web_browser)
    page.My_lab.click()
    assert page.login

#4 переход в Отложено
def test_postponed_click(web_browser):
    page = HeaderPage(web_browser)
    page.postponed.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'

#5 переход в Корзину
def test_basket_click(web_browser):
    page = HeaderPage(web_browser)
    page.basket.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cart/'

#6 переход в скидки сегодня
def test_click_discounts_today(web_browser):
    page = HeaderPage(web_browser)
    page.discounts_today.click()
    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'

#7 переход в Книги
def test_click_books(web_browser):
    page = HeaderPage(web_browser)
    page.books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'

#8 переход в Главное 2022
def test_click_main(web_browser):
    page = HeaderPage(web_browser)
    page.Main.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'

#9 переход в школа
def test_click_school(web_browser):
    page = HeaderPage(web_browser)
    page.School.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/'

#10 переход в Игрушки
def test_click_toys(web_browser):
    page = HeaderPage(web_browser)
    page.Toys.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'

#11 переход в Канцтовары
def test_click_stationery(web_browser):
    page = HeaderPage(web_browser)
    page.Stationery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'

#12 переход в Клуб
def test_click_club(web_browser):
    page = HeaderPage(web_browser)
    page.Club.click()
    assert page.get_current_url() == 'https://www.labirint.ru/club/'

#13 переход в Доставка и Оплата
def test_click_delivery_and_payment(web_browser):
    page = HeaderPage(web_browser)
    page.Delivery_and_payment.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'

#14 переход в Сертификаты
def test_click_certificates(web_browser):
    page = HeaderPage(web_browser)
    page.Certificates.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'

#15 переход в Рейтинги
def test_click_ratings(web_browser):
    page = HeaderPage(web_browser)
    page.Ratings.click()
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'

#16 переход в Новинки
def test_click_new_products(web_browser):
    page = HeaderPage(web_browser)
    page.New_products.click()
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'

#17 переход в Скидки
def test_click_discounts(web_browser):
    page = HeaderPage(web_browser)
    page.Discounts.click()
    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'

#18 переход в Контакты
def test_click_contacts(web_browser):
    page = HeaderPage(web_browser)
    page.Contacts.click()
    assert page.get_current_url() == 'https://www.labirint.ru/contact/'

#19 переход в Поддержка
def test_click_support(web_browser):
    page = HeaderPage(web_browser)
    page.Support.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'

#20 переход в 554 пункта самовывоза
def test_click_pickup_point(web_browser):
    page = HeaderPage(web_browser)
    page.PickupPoint.click()
    assert page.get_current_url() == 'https://www.labirint.ru/maps/'

#21 переход в соц.сеть Вк
def test_vk_click(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    vk = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-vk")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(vk)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirint_ru'

#22 переход в Youtube
def test_youtube_click(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    youtube = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon.b-header-b-social-e-icon-m-yt")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(youtube)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'

#23 переход в Одноклассники
def test_ok_click(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    ok = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-ok")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(ok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://ok.ru/labirintru'

#24 переход в Яндекс Дзен
def test_click_yandex_dzen(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    yandex_dzen = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-zen")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(yandex_dzen)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'

#25 переход в Телеграмм
def test_click_telegramm(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    telegramm = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-tg")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(telegramm)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://t.me/labirintru'

#26 переход в Tik Tok
def test_click_tik_tok(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    tik_tok = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-tiktok")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(tik_tok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru'

#27 переход в вк дети
def test_click_vk_deti(web_browser):
    page = HeaderPage(web_browser)
    social_network = web_browser.find_element_by_css_selector(
        ".b-header-b-sec-menu-e-link.b-labirint-all-social-network")
    vk_deti = web_browser.find_element_by_css_selector(".b-header-b-social-e-icon-m-vk-children")
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(vk_deti)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintdeti'













































