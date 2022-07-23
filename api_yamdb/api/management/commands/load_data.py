from csv import DictReader

from reviews.models import Review, Comment
from titles.models import Title, Category, Genre
from users.models import User


def import_users():
    for row in DictReader(open('./static/data/users.csv', encoding='utf-8')):
        User.objects.get_or_create(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            role=row['role'],
            bio=row['bio'],
            first_name=row['first_name'],
            last_name=row['last_name']
        )


def import_category():
    for row in DictReader(
            open('./static/data/category.csv', encoding='utf-8')
    ):
        Category.objects.get_or_create(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )


def import_genre():
    for row in DictReader(
            open('./static/data/genre.csv', encoding='utf-8')
    ):
        Genre.objects.get_or_create(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )


def import_title():
    for row in DictReader(
            open('./static/data/titles.csv', encoding='utf-8')
    ):
        Title.objects.get_or_create(
            id=row['id'],
            name=row['name'],
            year=row['year'],
            category=Category.objects.get(pk=row['category'])
        )


def import_review():
    for row in DictReader(
            open('./static/data/review.csv', encoding='utf-8')
    ):
        Review.objects.get_or_create(
            id=row['id'],
            title=Title.objects.get(pk=row['title_id']),
            text=row['text'],
            author=User.objects.get(pk=row['author']),
            score=row['score'],
            pub_date=row['pub_date']
        )


def import_comment():
    for row in DictReader(
            open('./static/data/comments.csv', encoding='utf-8')
    ):
        Comment.objects.get_or_create(
            id=row['id'],
            review=Review.objects.get(pk=row['review_id']),
            text=row['text'],
            author=User.objects.get(pk=row['author']),
            pub_date=row['pub_date']
        )
