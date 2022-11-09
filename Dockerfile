
FROM python:3.10

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN apt update && apt install -y libgl1-mesa-glx

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


