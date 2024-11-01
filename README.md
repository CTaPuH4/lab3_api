### Стек использованных технологий:

* Python
* Django
* Django REST framework

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/CTaPuH4/lab3_api.git
```

```
cd lab3_api/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры.
Запросы отправляются на эндпойнты c префиксом ```/api/```  например:
```http://127.0.0.1:8000```**/api/**```categories/```
