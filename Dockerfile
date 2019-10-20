FROM python:3.7
WORKDIR /bots
COPY config.py config.py
COPY twitter_bot.py twitter_bot.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV CONSUMER_KEY='Update_Me'
ENV CONSUMER_SECRET='Update_Me'
ENV ACCESS_TOKEN='Update_Me'
ENV ACCESS_TOKEN_SECRET='Update_Me'
ENV KEYWORD='UpdateMe'

CMD ["python", "twitter_bot.py"]