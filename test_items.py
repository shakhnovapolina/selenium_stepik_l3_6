import time

def test_placed_button_add_basket_different_languages(browser, option_lang):
    language = option_lang
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button is not None


