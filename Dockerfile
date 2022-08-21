FROM python:3.8-alpine
RUN mkdir /rad
RUN pip install flask
COPY . /rad
RUN rm /rad/Dockerfile

VOLUME ["/rad/data"]
EXPOSE 5000

ENTRYPOINT [ "sh" ]
CMD [ "/rad/start.sh" ]