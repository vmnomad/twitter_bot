FROM python:3.7-alpine
COPY ./bots /bots
RUN apk add --no-cache --update build-base && pip install -r /bots/requirements.txt
ENV CONSUMER_KEY='aftsFg5R37mx8BXf2XD91aSvY'
ENV CONSUMER_SECRET='01oLo5pSWj0UFXKtZFaOf9F65FHWS3ArP9guq05oWpLQFIO3cK'
ENV ACCESS_TOKEN='1185382197198381056-TSgKr0UANpH3ZA4FcAjTjt8fTCoEgu'
ENV ACCESS_TOKEN_SECRET='DBQhpFnbG3MRhfSsGKkBLbqhvxa2LK3Xx4w1dXYAOy7QW'
ENV KEYWORD='#100daysofk8s'
CMD ["python", "/bots/twitter_bot.py"]