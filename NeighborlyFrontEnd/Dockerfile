FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN apt update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]