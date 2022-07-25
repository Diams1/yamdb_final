FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]