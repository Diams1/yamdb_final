![Yamdb workflow](https://github.com/Diams1/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
![size](https://img.shields.io/github/repo-size/Diams1/yamdb_final?style=flat)
![docker_size](https://img.shields.io/docker/image-size/384134/yamdb_final?label=docker%20image%20size&style=flat)
# Yamdb_final
## Описание
Учебный проект Яндекс.Практикума. Основное приложение  -- ```api_yamdb```, которое дает возможность людям делиться отзывами о различных фильмах,
книгах, музыкальных коллекциях и других произведениях.

Проект упакован в Docker-контейнер и доступен по адресу http://<ip_address_сервера>/api/v1/

## Этот проект позволит Вам:
- Добавлять, просматривать, редактировать и удалять отзывы о произведениях.
- Добавлять, просматривать, редактировать и удалять комментарии к отзывам 
произведений.
- Ставить оценку произведениям от 1 до 10.

## DevOps.
По методологии CI/CD реализовано автоматическое тестирование кода, сборка в docker-контейнер и деплой образа на сервер.
Триггером является команда ```push``` в репозиторий проекта, при этом запускаются:
* Тестирование;
    * Проверка кода на PEP8
    * Запуск локальных тестов кода
* Сборка и выгрузка образа на <a href='https://hub.docker.com/'> DockerHub</a>
* Деплой образа на сервер, выполниние миграций и сбор статики
* Отправка уведомления в телеграм об успешном завершении

### Как запустить проект: 

####Для корректной работы CI/CD:
* Необходимо добавить(Fork) репозиторий к себе в профиль;
* Прописать переменные окружения в `Secrets-Actions` в настройках репозитория.
Необходимые переменные можно посмотреть в шаблоне `.env.template`

#### Клонируйте репозиторий:
```bash
git clone https://github.com/Diams1/yamdb_final
```
#### Создайте файл ```.env``` в каталоге infra и заполните данными по шаблону `.env.template`:
```bash
touch /infra/.env
```
```bash
nano /infra/.env
```

#### Установите на удаленном сервере <a href='https://docs.docker.com/get-docker/'> Docker</a>.
**Скопируйте файлы `docker-compose.yaml` и `nginx/default.conf` из репозитория на сервер в
`home/<ваш_username>/docker-compose.yaml` и `home/<ваш_username>/nginx/default.conf` соответственно.**
```bash
scp docker-compose.yaml username@host:home/<ваш_username>/docker-compose.yaml
```
```bash
scp nginx/default.conf username@host:home/<ваш_username>/nginx/default.conf
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

## Документация к API REDOC
 http://<ip_address_сервера>/redoc/

### Примеры запросов к API.

##### Аутентификация выполняется через Simple JWT.  
Для получения кода подтверждения регистрации отправьте POST запрос с логином и e-mail на эндпойнт:
```
http://<ip_address_сервера>/api/v1/auth/signup/
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
http://<ip_address_сервера>/api/v1/auth/token/
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
http://<ip_address_сервера>/api/v1/users/me/
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
http://<ip_address_сервера>/api/v1/titles/
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

Ответ:
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

## Для разработки проекта использовалось:


![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)
  
## Авторы:
_Alexey Chinenkov_ :
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Diams1) 
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Diams)
