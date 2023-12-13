FROM python:3.11
RUN pip install fastapi mangum uvicorn
RUN pip freeze > requirements.txt
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN npm i -g serverless
WORKDIR /code
COPY . /code/
RUN serverless plugin install -n serverless-python-requirements
