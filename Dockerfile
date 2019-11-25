# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to / app
WORKDIR .

# Copy the current directory contents into the container at / app
ADD . /app
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ./app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 443

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# CMD ["python", "flask-api.py"]
CMD ["ls -al"]