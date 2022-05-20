from pages.footer_page import FooterPage

#1 Проверка перехода в App Store
def test_app_store_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.app_Store.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://apps.apple.com/ru/app/%D0%BB%D0%B0%D0%B1%D0%B8%D1%80%D0%B8%D0%BD%D1%82-%D1%80%D1%83-%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD/id1008650482'

#2 Проверка перехода в Google Play
def test_google_play_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.google_Play.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://play.google.com/store/apps/details?id=ru.labirint.android'

#3 Проверка перехода в App_Gallery
def test_app_gallery(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.app_Gallery.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://appgallery.huawei.com/app/C101184737?appId=C101184737&source=appshare&subsource=C101184737'

#4 проверка перехода в соцсеть Вконтакте
def test_vk_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.VK.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirint_ru'

#5 проверка перехода в соцсеть Вконтакте.Дети
def test_vk_children_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.VKchildren.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintdeti'

#6 проверка перехода в соцсеть Youtube
def test_youtube_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'

#7 проверка перехода в соцсеть Одноклассники
def test_ok_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.ok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://ok.ru/labirintru'

#8 проверка перехода в соцсеть Яндекс.Дзен
def test_dzen_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.Dzen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'

#9 проверка перехода в соцсеть Telegram
def test_telegram_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.telegram.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://t.me/labirintru'

#10 проверка перехода в соцсеть TikTok
def test_tiktok_click(web_browser):
    page = FooterPage(web_browser)
    page.scroll_down()
    page.TikTok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru'








