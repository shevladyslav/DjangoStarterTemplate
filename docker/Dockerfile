FROM python:3.10.11

WORKDIR /code

COPY requirements/ /code/

RUN pip install -r local.pip

COPY . /code/

EXPOSE 8000

CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
