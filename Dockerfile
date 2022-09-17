FROM python:3.9

ENV HOME /app
WORKDIR HOME

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
COPY entrypoint.sh .

CMD ["sh", "entrypoint.sh"]