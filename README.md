### �������� �������:
������ API ��� ������� ���������� Yatube.

### ������ �������:

����������� ����������� � ������� � ���� � ��������� ������:

```
git@github.com:ALoshchilov/api_final_yatube.git
```

```
cd api_final_yatube
```

C������ � ������������ ����������� ���������:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

���������� ����������� �� ����� requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

��������� ��������:

```
python3 manage.py migrate
```

��������� ������:

```
python3 manage.py runserver
```

### ������� ������� API:

��������� ������ ���� ����������.
```
GET http://127.0.0.1:8000/api/v1/posts/
```



��������� ������ ���������� � ����������.
```
GET http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100
```



��������� ����� � ID 1. ����� �� ��������� ����� ������ ����� �����.
���� image � group �����������.
```
PATCH http://127.0.0.1:8000/api/v1/posts/1/
```
���� �������:
```
body:
{
    "text": "Some text",
    "image": <image bytecode>,
    "group": <group_id>
}
```

��������� ������ ������������ � ����� � ID 1.
```
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

�������� ����������� � ID 2 � ����� � ID 1. �������� ������ ������ �����������.
```
DELETE http://127.0.0.1:8000/api/v1/posts/1/comments/2/
```

��������� ������ �����.
```
GET http://127.0.0.1:8000/api/v1/groups/
```

�������� �� ������ � ������� username123.
```
POST http://127.0.0.1:8000/api/v1/follow/
```
���� �������:
```
body:
{
  "following": "username123"
}
```

��������� ������ ��� ������������ user � ������� qwerty
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
```
���� �������:
```
{
"username": "user",
"password": "qwerty"
}
```
