FROM python:3.7-alpine
COPY ./bots /bots
RUN apk add --no-cache --update build-base && pip install -r /bots/requirements.txt && source /bots/envvars
RUN echo "Hello World 1"
CMD ["python", "/bots/twitter_bot.py"]
