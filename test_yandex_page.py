import allure


@allure.step("Тестирование страницы 'Яндекса'")
def test_open_main_page(app):
    app.open_search_stroke()
    app.close_window()
    app.get_request()