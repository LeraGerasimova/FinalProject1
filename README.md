# FinalProject1
Финальное задание курса "Тестировщик-автоматизатор на Python (QAP)" Объект тектирования: https://www.labirint.ru

tests/ содержит тесты для главной старницы (отдельно для header, body, footer) и корзины. 

pages/base.py содержит реализацию шаблона PageObject для Python 

pages/elements.py содержит вспомогательный класс для определения веб-элементов на веб-страницах

Описание test_body_page.py В файле 13 тестов.
Были проведены проверки перехода на главные разделы в body сайта. 
Два теста отмечены маркером @pytest.mark.xfail, так как были найдены баги:
1.При исполнении теста отстутствует раздел "Нужные учебники для вас в этом году".
2.При исполнении теста отстутствует раздел "Нас ценит"

Описание test_footer_page.py
В файле 10 тестов. Все тесты пройдены. 
Были проведены проверки перехода на соц.сети и магазины в footer cайта.

Описание test_header_page.py
В файле 27 тестов. Все тесты пройдены. 
Были проведены проверки перехода на разделы в header сайта.

Описание test_basket.py В файле 7 тестов. Все тесты пройдены. Были проведены проверки:

1.Добавление книги в корзину
2.Увеличение количества книг в корзине
3.Проверка очистки корзины
4.Проверка восстановления удаленных товаров
5.Проверка разделов: как сделать заказ, как получить заказ, как оплатить заказ.

Всего было проведено 57 тестов.

Как запускать тесты: Установить все внешние зависимости командой pip install -r requirements.txt

Скачать версию Selenium WebDriver, совместимую с вашим браузером (тесты проводились в браузере Google Chrome)

Команды необходимо выполнить для запуска тестов:

pytest -v --driver Chrome --driver-path C:/Users/Public/Driver/chromedriver.exe tests/test_header_page.

pytest -v --driver Chrome --driver-path C:/Users/Public/Driver/chromedriver.exe tests/test_body_page.py

pytest -v --driver Chrome --driver-path C:/Users/Public/Driver/chromedriver.exe tests/test_footer_page.py

pytest -v --driver Chrome --driver-path C:/Users/Public/Driver/chromedriver.exe tests/test_basket.py

где C:/Users/Public/Driver/ находится путь к драйверу Selenium для текущей ОС
