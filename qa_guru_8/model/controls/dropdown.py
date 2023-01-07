from selene import have
from selene.support.shared import browser


def select_option(selector, text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)
    ).click()
