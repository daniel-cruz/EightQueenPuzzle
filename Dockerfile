FROM python

WORKDIR /eightqueens
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD [ "python3", "-m" , "run", "--host=0.0.0.0"]
