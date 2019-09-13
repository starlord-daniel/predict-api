# In the first part of our Dockerfile, we define the base Docker Image we want to use for the container.
FROM python:3.6-slim

# move data to the image. Left is location on your machine, right is location in the container
COPY requirements.txt requirements.txt
COPY . .

# Install app dependencies - rerun when you edit requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for container accessibility. You still have to add -p 8000:8000 to the docker run command
EXPOSE 8000
ENTRYPOINT ["python"]

# start the app.py file 
CMD ["run.py"]