from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest


link = "http://localhost:8000/"
browser = webdriver.Chrome()
browser.get(link)


def get_id_chat_one():
    new_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    element = browser.find_element(By.XPATH, '/html/body/ul/li[1]').text
    return element[0:21]


def get_id_chat_two():
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    element = browser.find_element(By.XPATH, '/html/body/ul/li[2]').text
    return element[0:21]


def your_id_one_and_two(number_windom: int):
    new_window = browser.window_handles[number_windom]
    browser.switch_to.window(new_window)
    return browser.find_element(By.XPATH, '//span[@id="ws-id"]').text


def message_test(message):
    try:
        write_element = browser.find_element(By.XPATH, '//input[@id="messageText"]')
        write_element.send_keys(message)
        browser.find_element(By.XPATH, '//button').click()
    except NoSuchElementException:
        return f"отсутствует элемент"


def switch_to_another_tab():
    browser.execute_script("window.open('http://localhost:8000/')")
