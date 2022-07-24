FROM python:3.7-slim
WORKDIR /app
COPY . .


WORKDIR /app/api_yamdb
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --no-input
RUN python3 manage.py loaddata fixtures.json
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]