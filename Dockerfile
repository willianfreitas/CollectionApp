FROM ubuntu:20.04

WORKDIR /home/root

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

ENV PORT 8000
EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ADD . .

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]