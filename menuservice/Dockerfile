FROM python:3.8

WORKDIR /usr/src/menuservice/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]