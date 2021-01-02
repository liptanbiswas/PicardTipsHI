FROM python:3.8-slim

COPY requirements.txt /opt/picardtipshi/requirements.txt

COPY *.py /opt/picardtipshi/

COPY run.sh /opt/picardtipshi/run.sh

RUN chmod +x /opt/picardtipshi/run.sh

WORKDIR /opt/picardtipshi/

RUN pip install -r requirements.txt

CMD ["/bin/sh", "-c", "/opt/picardtipshi/run.sh"]
