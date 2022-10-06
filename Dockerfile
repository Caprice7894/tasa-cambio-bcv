FROM python:3.10-alpine3.16
RUN apk add --no-cache python3 bash curl gawk
WORKDIR /app
ADD requirements.txt /app
RUN pip install flask
ADD . /app
CMD ["python3", "app.py", "--host", "0.0.0.0"]
EXPOSE 80
