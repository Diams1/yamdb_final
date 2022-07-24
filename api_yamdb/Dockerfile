FROM python:3.7-slim
WORKDIR /app/api_yamdb
COPY requirements.txt /app/api_yamdb
RUN pip3 install -r /app/api_yamdb/requirements.txt --no-cache-dir
COPY . /app/api_yamdb
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
