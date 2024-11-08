FROM python:3.9-slim 
WORKDIR /Docker1


COPY /database_files/databasefunctions.py /Docker1/database_files/databasefunctions.py
COPY app.py app.py
COPY /database_files/initdatabase.py /Docker1/database_files/initdatabase.py 


# Copy requirements.txt from docker_files directory into the container
COPY docker_files/requirements.txt /Docker1/requirements.txt

# Install Python dependencies inside Docker
RUN pip3 install -r /Docker1/requirements.txt

EXPOSE 5000

CMD python3 /Docker1/database_files/initdatabase.py && python3 app.py
