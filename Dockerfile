
FROM python:latest
RUN mkdir /app
COPY app.py /app
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./app/app.py" ]


