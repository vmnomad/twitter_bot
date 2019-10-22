FROM python:3.7-alpine
COPY ./bots /bots
RUN apk add --no-cache --update build-base && pip install -r /bots/requirements.txt && source /bots/envvars
CMD ["python", "/bots/twitter_bot.py"]
