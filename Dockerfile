
FROM python:latest

COPY ./files/requirements.txt /requirements.txt

RUN pip install --no-cache -r /requirements.txt

RUN cd /files/justforfun/

EXPOSE 8080
EXPOSE 4443

CMD ["/bin/bash"]

