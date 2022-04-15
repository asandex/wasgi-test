FROM python:3.10-alpine

WORKDIR /usr/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
COPY ./src .

CMD [ \
    "gunicorn", "wasgi_test.asgi:application", \
    "-k", "uvicorn.workers.UvicornWorker", \
    "-w", "1", \
    "--bind", "0.0.0.0:8000" \
]
