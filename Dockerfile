FROM python:3.8-slim

COPY requirements.txt /opt/picardtipshi/requirements.txt

COPY *.py /opt/picardtipshi/

WORKDIR /opt/picardtipshi/

RUN pip install -r requirements.txt

CMD ["python", "/opt/picardtipshi/main.py"]
