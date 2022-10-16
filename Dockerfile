FROM python:3.9.14

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip 
RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml Makefile /app/

RUN make install

COPY . .

RUN make migrate

EXPOSE 8000

CMD [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]