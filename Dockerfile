FROM python:3.7-alpine
COPY ./bots /bots
RUN apk add --no-cache --update build-base && pip install -r /bots/requirements.txt
ENV CONSUMER_KEY='UpdateMe'
ENV CONSUMER_SECRET='UpdateMe'
ENV ACCESS_TOKEN='UpdateMe'
ENV ACCESS_TOKEN_SECRET='UpdateMe'
ENV KEYWORD='#100daysofk8s'
CMD ["python", "/bots/twitter_bot.py"]