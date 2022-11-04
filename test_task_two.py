# import json
# import sqlite3
import requests
from examples import EXAMPLES_PING, EXAMPLES_GENRES, EXAMPLES_GET_DATA_ID


def test_ping_page_status_code_and_content():
    response = requests.get('http://localhost:8000/ping_page/ping')
    assert response.status_code == 200
    assert response.json() == EXAMPLES_PING, f'ВЕРНУЛ: {response.json()}'
    assert response.headers.get('server') == 'uvicorn'


def test_get_genres():
    response = requests.get('http://localhost:8000/ping_page/get_genres')
    assert response.status_code == 200, f"ВЕРНУЛ: {response.status_code}"
    assert response.json() == EXAMPLES_GENRES, f"ВЕРНУЛ: {response.json()}"
    assert response.headers.get('content-length') == str(416)


def test_get_data_id():
    response = requests.get('http://localhost:8000/ping_page/get_data/1')
    assert response.status_code == 200, f"ВЕРНУЛ: {response.status_code}"
    assert response.json() == EXAMPLES_GET_DATA_ID, f"ВЕРНУЛ: {response.json()}"
    assert response.json().get('count') == 1108, f" ВЕРНУЛ: {response.json().get('count')}"


# def test_get_sql_request():
#     connection = sqlite3.connect('task_2/test.db')
#     cursor = connection.cursor()
#     string = f"SELECT DISTINCT Name, Composer, GenreId FROM tracks WHERE GenreId = {1} AND Composer <> 'None' ORDER BY Composer"
#     # res = cursor.execute(string)
#     records = cursor.execute("SELECT * FROM tracks")
#     assert records == 'test'
