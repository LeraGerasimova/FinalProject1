import os
from pages.base import WebPage
from pages.elements import WebElement

class FooterPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.labirint.ru/"
        super().__init__(web_driver, url)

    # Локаторы

    #Магазин App Store
    app_Store = WebElement(css_selector = "[data-event-content='App Store']")
    # Магазин Google Play
    google_Play = WebElement(css_selector = "[data-event-content='Google Play']")
    # Магазин App Gallery
    app_Gallery = WebElement(css_selector = "[data-event-content='App Gallery']")
    #ВКонтакте
    VK = WebElement(css_selector = "[data-event-content='ВКонтакте']")
    #ВКонтакте. Дети
    VKchildren = WebElement(css_selector = "[data-event-content='ВКонтакте. Дети']")
    #Ютьюб
    youtube = WebElement(css_selector = "[data-event-content='Ютьюб']")
    #Одноклассники
    ok = WebElement(css_selector = "[data-event-content='Одноклассники']")
    #Дзен
    Dzen = WebElement(css_selector = "[data-event-content='Дзен']")
    #Телеграм
    telegram = WebElement(css_selector = "[data-event-content='Телеграм']")
    #ТикТок
    TikTok = WebElement(css_selector = "[data-event-content='ТикТок']")







