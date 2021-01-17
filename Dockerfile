FROM centos:centos7
RUN echo "ACTUALIZANDO CENTOS"
RUN yum update -y

RUN echo "INSTALANDO PYTHON3"
RUN yum install -y python3

RUN echo "INSTALANDO DEPENDENCIAS"
RUN pip3 install djangorestframework
RUN pip3 install djongo
RUN pip3 install dnspython
RUN pip3 install django-cors-headers

RUN echo "EMPAQUETANDO PROYECTO"
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN echo "MIGRACIONES"
RUN python3 manage.py makemigrations restaurants
RUN python3 manage.py migrate

RUN echo "INSTALACION FINALIZADA"
CMD ["python3", "./manage.py runserver 0.0.0.0:$PORT"]
RUN echo "SERVIDOR LEVANTADO"
