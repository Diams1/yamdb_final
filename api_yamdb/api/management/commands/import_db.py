from django.core.management import BaseCommand

from reviews.models import Comment, Review
from titles.models import Category, Genre, Title
from users.models import User
from .load_data import (
    import_users,
    import_category,
    import_genre,
    import_title,
    import_review,
    import_comment
)

DB_TABLES = [User, Title, Category, Comment, Genre, Review]


class Command(BaseCommand):
    help = "Импорт данных из /static/data"

    def handle(self, *args, **options, ):
        for table in DB_TABLES:
            if table.objects.exists():
                print('В базе уже есть данные.\n'
                      'Перед импортом убедитесь, что таблица пуста.')
                return

        print("Загрузка данных:")
        try:
            import_users()
            print('Загрузка пользователей завершена.')
            import_category()
            print('Загрузка категорий завершена.')
            import_genre()
            print('Загрузка жанров завершена.')
            import_title()
            print('Загрузка произведений завершена.')
            import_review()
            print('Загрузка отзывов завершена.')
            import_comment()
            print('Загрузка комментариев завершена.')
        except ValueError:
            print('Ошибка в значении')
        except Exception as e:
            print(f'Фатальная ошибка!: {e}')
        else:
            print('Импорт успешно завершен.')
