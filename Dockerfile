
FROM python:3.12

RUN python -m pip install --upgrade pip

#
# This is used by the OpenCV module for image manipulation.
#
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY bin /app/bin
COPY bin/entrypoint.sh /

COPY main.py /app
COPY pytest.sh /app
COPY lib/ /app/lib/
COPY tests/ /app/tests/
COPY private/ /app/private/
COPY static/ /app/static/
COPY img/ /app/img


WORKDIR /app

EXPOSE 80/tcp

ENV PORT=80

ENTRYPOINT [ "/entrypoint.sh" ]
