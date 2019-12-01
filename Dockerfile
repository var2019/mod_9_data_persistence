# Use an official Python runtime as a parent image
FROM laudio/pyodbc:1.0.4

# Set the working directory to / app
WORKDIR /app

# Copy the current directory contents into the container at / app
ADD *.py /app/
ADD *.sh /app/
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
ENTRYPOINT [ "python" ]
CMD ["flask_api.py"]
