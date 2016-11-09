FROM python

WORKDIR /app

COPY . .
RUN pip install --upgrade pip && \
		pip install -r requirements.txt

EXPOSE 8000
CMD /bin/sh docker-entrypoint.sh
