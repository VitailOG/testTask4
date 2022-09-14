FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY r.txt .

RUN pip install --no-cache-dir --upgrade pip && pip install -r r.txt

COPY . .

EXPOSE 8000
