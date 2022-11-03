# import requests
# from task_2.examples import EXAMPLES
#
#
# def test_ping_page_status_code():
#     response = requests.get('http://localhost:8000/ping_page/ping')
#     assert response.status_code == 200
#
#
# def test_ping_page_content():
#     response = requests.get('http://localhost:8000/ping_page/ping')
#     assert response.content == EXAMPLES, response.content
