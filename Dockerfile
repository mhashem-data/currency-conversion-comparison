FROM python:3.12-slim

WORKDIR /app

COPY currencies_converter.py .

RUN pip install requests

CMD ["python", "currencies_converter.py"]