FROM python:3.9

RUN mkdir /reports_landing_page

WORKDIR /reports_landing_page

ADD . /reports_landing_page/

RUN pip install -r requirements.txt
