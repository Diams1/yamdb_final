FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir
WORKDIR /app/api_yamdb
COPY /app/api_yamdb/static/redoc.yaml /app/static/redoc.yaml
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
