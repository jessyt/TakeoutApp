FROM python:3.8

WORKDIR /usr/src/userservice/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

CMD ["python", "app.py"]