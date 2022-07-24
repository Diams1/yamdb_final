![Yamdb workflow](https://github.com/Diams1/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Yamdb_final
## Описание
Учебный проект Яндекс.Практикума. Основное приложение  -- ```api_yamdb```, которое дает возможность людям делиться отзывами о различных фильмах,
книгах, музыкальных коллекциях и т.д.

Проект упакован в Docker-контейнер.
## Документация к API REDOC
 http://127.0.0.1/redoc/

## Этот проект позволит Вам:
- Добавлять, просматривать, редактировать и удалять отзывы о произведениях.
- Добавлять, просматривать, редактировать и удалять комментарии к отзывам 
произведений.
- Ставить оценку произведениям от 1 до 10.
### Как запустить проект: 

#### Клонируйте репозиторий:
```bash
git clone https://github.com/Diams1/infra_sp2
```
#### Создайте файл ```.env``` в каталоге infra и заполните данными по шаблону:
```bash
touch /infra/.env
```
```bash
nano /infra/.env
```
шаблон:
```Python
SECRET_KEY_SETTINGS='set_your_secret_key'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password   # укажите свой пароль
DB_HOST=db
DB_PORT=5432
```

#### Установите <a href='https://docs.docker.com/get-docker/'> Docker</a> и запустите.
#### Для сборки и запуска контейнера из образа выполните команду:
```bash
docker-compose up -d --build
```
Для сборки образа будут выполнены инструкции из файла ```docker-compose.yaml```

#### Выполните миграции:
```bash
docker-compose exec web python manage.py migrate
```
#### Выгрузите статику и медиа в рабочие каталоги:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```
#### Импортируйте данные из CSV в БД (опционально) :
```bash
docker-compose exec web python manage.py import_db
```
#### Импортируйте данные из бэкапа БД (опционально):
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```
#### Создайте суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

#### Для остановки контейнера выполните команду:
```bash
docker-compose stop
```

### Примеры запросов к API.

##### Аутентификация выполняется через Simple JWT.  
Для получения кода подтверждения регистрации отправьте POST запрос с логином и e-mail на эндпойнт:
```
http://localhost/api/v1/auth/signup/
```

POST-запрос:
```JSON
{
    "email": "email@example.com",
    "username": "my_login"
}
```

Ответ:
```JSON
{
    "email": "email@example.com",
    "username": "my_login"
}
```

##### Для получения токена отправьте POST запрос с логином и полученным по e-mail кодом подтверждения на эндпойнт:
```
http://localhost/api/v1/auth/token/
```

POST-запрос:
```JSON
{
    "username": "my_login",
    "confirmation_code": "code"
}
```

Ответ:
```JSON
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2b2tlb90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1OTc4OTAwOSwiaWF0IjoxNjU4MDYxMDA5LCJqdGkiOiJkNTUyNTJlODQ0OGI0MDExYjFjOGYwZDYxOGU2ZjAxZCIsInVzZXJfaWQiOjF9.IVjgYCbZiQ_kdraTYIz4VdYYpZoh7kTMxpmjjJ1tkIg",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2b2tlb90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4OTI1MDA5LCJpYXQiOjE2NTgwNjEwMDksImp0aSI6ImIzZDViMmY2YjExZjQxMTM4NTk1NWVmMzg5NmZmM2JkIiwidXNlcl9pZCI6MX0.dEfpwO3ZBA62R6lH6ybHx3KxCZU9PgQCoXvaEsl5UyI"
}
```

##### Для редактирования своего профайла отправьте PATCH запрос на эндпойнт:
```
http://localhost/api/v1/users/me/
```
PATCH-запрос:
```JSON
{
    "username": "my_login",
    "email": "email@example.com",
    "role": "user",
    "bio": "I'm an alcoholic",
    "first_name": "Ilon",
    "last_name": "Mask"
}
```

Ответ:
```JSON
{
    "username": "my_login",
    "email": "email@example.com",
    "role": "user",
    "bio": "I'm an alcoholic",
    "first_name": "Ilon",
    "last_name": "Mask"
}
```

##### GET запрос для получения списка произведений:
```
http://localhost/api/v1/titles/
```

Ответ:
```JSON
{
    "count": 32,
    "next": "http://web:8000/api/v1/titles/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Побег из Шоушенка",
            "year": 1994,
            "rating": 10,
            "description": null,
            "category": {
                "name": "Фильм",
                "slug": "movie"
            },
            "genre": []
        },
        {
            "id": 2,
            "name": "Крестный отец",
            "year": 1972,
            "rating": 4,
            "description": null,
            "category": {
                "name": "Фильм",
                "slug": "movie"
            },
            "genre": []
        },
...
```


##### Получение информации о произведении GET запрос:
```
http://localhost/api/v1/titles/{titles_id}/
```

Response:
```JSON
{
    "id": 9,
    "name": "Форрест Гамп",
    "year": 1994,
    "rating": 7,
    "description": null,
    "category": {
        "name": "Фильм",
        "slug": "movie"
    },
    "genre": []
}
```

##### Для добавления отзыва о произведении отправьте POST запрос:
```
http://localhost/api/v1/titles/{title_id}/reviews/
```
POST-запрос:
```JSON
{
    "genre": ["ballad"],
    "category": "book",
    "name": "Some name.",
    "year": 1999
}
```
Ответ:
```JSON
{
    "id": 33,
    "genre": [
        "ballad"
    ],
    "category": "book",
    "name": "Some name.",
    "year": 1999,
    "description": null,
    "rating": null
}
```

## Что использовалось для создания проекта:
 - Docker compose
 - Postgres
 - Nginx
 - Gunicorn
 - Python 3.9
 - Django 2.2
 - Django REST framework 3.12
 - JWT token
  
## Авторы:
 - Алексей Чиненков : <a href='https://github.com/Diams1'> GitHub</a>, <a href='https://t.me/Diams'> Telegram</a>
