# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]

# Set the working directory in the container
#WORKDIR /app

# Copy the requirements file into the container at /app
#COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
#COPY . /app

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME my-flask-app

# Run app.py when the container launches
#CMD ["python3", "app.py"]
