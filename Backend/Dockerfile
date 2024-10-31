FROM python:3.9-slim
WORKDIR /Docker1
COPY main.py main.py
COPY requirements.txt requirements.txt
COPY PetFuc.py PetFuc.py
COPY UserFuc.py UserFuc.py
COPY test_main.py test_main.py
RUN pip3 install -r requirements.txt
CMD [ "python3", "main.py" ]


