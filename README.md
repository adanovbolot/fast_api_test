# для запуска тестов

    git clone git@github.com:adanovbolot/fast_api_test.git
    
    python -m venv myenv
    
    pip install -r requirements.txt

    source venv/bin/activate.fish


для запуска 1 теста

    cd task_1
    
    python main.py

    cd ..
    
    pytest -vv -s test_task_one.py


# TESTCASE LIST
## 1 task

cd /tast_1/main.py | test file - test_main.py

test - test_message_and_send

кейс №1

    идентификатор тест-кейса - 001
    Название - проверка схожести id chat-a
    шаги - тест кейса
        1 шаг - зайти на http://localhost:8000
        2 шаг - открыть второй http://localhost:8000
                для соединение чата
        3 шаг - вернуться на первую вкладку
        4 шаг - написать письмо
        5 шаг - нажать на send
        6 шаг - открыть вторую вкладку для проверки 
        
    Ожидаемый результат - сравнить id чата

test - test_status_code_and_headers

кейс №2

    идентификатор тест-кейса - 002
    Название - проверка статус кода на get запрос
    шаги - тест кейса
        1 шаг - запрос на http://localhost:8000 | GET запрос
        2 шаг - сравнить статус код
    Ожидаемый результат - status code 200

test - test_your_id_chat 

кейс №3

    идентификатор тест-кейса - 003
    Название - проверка ровности id
    шаги - тест кейса
        1 шаг - открыть http://localhost:8000
        2 шаг - открыть второй http://localhost:8000
                для соединение чата
        3 шаг - взять your id второй закладки
        4 шаг - вернуться на первую закладку
        5 шаг - взять your id первой закладки
        6 шаг - сравнить id на противоположность 
    Ожидаемый результат - должен вернуть не равный id