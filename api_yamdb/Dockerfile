FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir