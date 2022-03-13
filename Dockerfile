FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./
COPY ./ ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]