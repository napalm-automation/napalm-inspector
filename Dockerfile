FROM python:3.6

COPY . /napalm-inspector

RUN pip install /napalm-inspector

ENV FLASK_APP napalm_inspector

ENTRYPOINT flask run --host=0.0.0.0