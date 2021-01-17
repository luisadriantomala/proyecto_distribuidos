FROM python:3

RUN mkdir /code
WORKDIR /code
COPY . /code/


RUN echo "INSTALANDO DEPENDENCIAS"
RUN pip install djangorestframework
RUN pip install djongo
RUN pip install dnspython
RUN pip install django-cors-headers