
FROM python:3.10

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY bin /app/bin
COPY bin/entrypoint.sh /

COPY main.py /app
COPY pytest.sh /app
COPY lib/ /app/lib/
COPY tests/ /app/tests/
COPY private/ /app/private/
COPY static/ app/static/


WORKDIR /app

EXPOSE 80/tcp

ENV PORT=80

ENTRYPOINT [ "/entrypoint.sh" ]


