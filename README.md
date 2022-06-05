### Описание проекта:
Проект API для сервиса публикаций Yatube.

### Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:ALoshchilov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

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

### Примеры вызывов API:

Получение списка всех публикаций.
```
GET http://127.0.0.1:8000/api/v1/posts/
```



Получение списка публикаций с пагинацией.
```
GET http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100
```



Изменение поста с ID 1. Права на изменение имеет только автор поста.
Поля image и group опциональны.
```
PATCH http://127.0.0.1:8000/api/v1/posts/1/
```
Тело запроса:
```
body:
{
    "text": "Some text",
    "image": <image bytecode>,
    "group": <group_id>
}
```

Получение списка комментариев к посту с ID 1.
```
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Удаление комментария с ID 2 к посту с ID 1. Доступно только автору комментария.
```
DELETE http://127.0.0.1:8000/api/v1/posts/1/comments/2/
```

Получение списка групп.
```
GET http://127.0.0.1:8000/api/v1/groups/
```

Подписка на автора с логином username123.
```
POST http://127.0.0.1:8000/api/v1/follow/
```
Тело запроса:
```
body:
{
  "following": "username123"
}
```

Получение токена для пользователя user с паролем qwerty
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
```
Тело запроса:
```
{
"username": "user",
"password": "qwerty"
}
```
