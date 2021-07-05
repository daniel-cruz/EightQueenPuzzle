FROM python

WORKDIR /eightqueens
COPY requirements.txt requirements.txt
RUN pip install --proxy="http://EOLVB:Biotec2021@10.11.24.70:8080" -r requirements.txt
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
