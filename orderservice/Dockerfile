FROM python:3.8

WORKDIR /usr/src/orderservice/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]