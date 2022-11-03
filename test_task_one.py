from task_1.DESIGN import get_id_chat_one, switch_to_another_tab, \
    message_test, get_id_chat_two, your_id_one_and_two, browser
import requests


def test_message_and_send():
    switch_to_another_tab()
    message_test('test')
    chat_id_one = get_id_chat_one()
    chat_id_two = get_id_chat_two()
    assert chat_id_one == chat_id_two, f'чат id не сходятся'


def test_your_id_chat():
    switch_to_another_tab()
    id_chat_one = your_id_one_and_two(1)
    id_chat_two = your_id_one_and_two(0)
    assert id_chat_one != id_chat_two, f"чат id не сходятся: 1 {id_chat_one}, 2 {id_chat_two}"


def test_status_code_and_headers():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200, f'статус код вернул :{response.status_code}'
    browser.quit()
