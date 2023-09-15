FROM python:3.10.7-bullseye


ENV PYTHONUNBUFFERED 1
ENV PYTOHDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
