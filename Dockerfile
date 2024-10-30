FROM python:3.9-slim

WORKDIR /
RUN pip install python-telegram-bot --upgrade
COPY . .
CMD ["python","main.py"]
