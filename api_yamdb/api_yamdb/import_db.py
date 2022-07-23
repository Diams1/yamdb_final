import csv
from reviews.models import Review, Comment
from users.models import User

with open("static/data/review.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Review.objects.get_or_create(
            id=row[1],
            title_id=row[2],
            text=row[3],
            author_id=row[4],
            score=row[5],
            pub_date=row[6],
        )

with open("static/data/comments.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Comment.objects.get_or_create(
            id=row[1],
            review_id=row[2],
            text=row[3],
            author_id=row[4],
            pub_date=row[5],
        )

with open("static/data/users.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = User.objects.get_or_create(
            id=row[1],
            username=row[2],
            email=row[3],
            role=row[4],
            bio=row[5],
            first_name=row[6],
            last_name=row[7],
        )
