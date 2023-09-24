
FROM python:3.9.7
WORKDIR /app
COPY . /app

#download using no cache
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

# run the application
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
