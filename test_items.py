"""
Ссылка;
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

Запуск:
pytest --language=es test_items.py
"""
import pytest
from selenium import webdriver
import time

def test_find_card_button(browser):
    try: 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(3)
        browser.find_element_by_css_selector("#login_link")
        button=browser.find_element_by_class_name('btn-add-to-basket')
        assert button is not None, 'asserError'
    finally:
        browser.close()
