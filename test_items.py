from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_link(browser):
    browser.get(link)
    time.sleep(5)

    css_selector = "form.add-to-basket .btn.btn-lg.btn-primary.btn-add-to-basket"
    def test_check_exists_by_css_selector(css_selector):
        try:
            browser.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            return False
        return True
    assert test_check_exists_by_css_selector(css_selector) == True, "корзинка не найдена"

