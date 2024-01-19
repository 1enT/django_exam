# django_exam

## Подготовка виртуального окружения

- `python -m venv venv` - создание виртуального окружения
- `venv\Scripts\activate` - войти в виртуальное окружения (для пользователей Windows)
- `pip install -r requirements.txt` - установка зависимостей

## Настройка базы данных
django_exam работает с PostgreSQL, поэтому он должен быть установлен на ПК. Установить его можно с [официального сайта](https://www.postgresql.org/download/)

Username, password и port для подключения к БД установлены на значения по умолчанию, которые Postgres создает при установке.
Если они отличаются, необходимо самостоятельно изменить данные для подключения к БД в настройках проекта. В файле `myproject/settings.py` 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_test',
        'USER': '',  # Имя пользователя
        'PASSWORD': '', # Пароль
        'HOST': 'localhost',
        'PORT': # Порт
    }
}
```

Теперь в Postgres необходимо создать базу данных с названием django_test

## Применение миграций

Чтобы создать модели, необходимо ввести `python manage.py migrate`

## Админ-панель

Чтобы пользоваться админ-панелью, необходимо создать суперпользователя
`python manage.py createsuperuser`
Дальше следуйте инструкциям на экране

## Запуск проекта
`python manage.py runserver` - запуск локального сервера на 127.0.0.1:8000