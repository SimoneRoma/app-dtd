# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Set Env Variable for MySQL Connection
ENV env_name $USER
ENV env_name $HOST
ENV env_name $PASS

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/app.py .

# Expose the port on which the application will listen
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]
