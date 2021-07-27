FROM python:3.8.5
EXPOSE 5000
ADD . /app
WORKDIR /app
COPY . .
RUN pip install -r ./src/requirements.txt
ENV FLASK_APP=./src/main.py
#
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
