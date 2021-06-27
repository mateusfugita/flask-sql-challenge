FROM python:3.6-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python database/migration.py
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]