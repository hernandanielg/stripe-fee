FROM python

EXPOSE 8000
WORKDIR /app

COPY . .
RUN pip install --upgrade pip && \
		pip install -r requirements.txt

CMD /bin/sh docker-entrypoint.sh
