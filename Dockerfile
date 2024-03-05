# Use a lean Python base image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# COPY requirements.txt ./

RUN pip install flask psycopg2 flask_sqlalchemy

# Copy your application files
COPY . .

# Install packages directly using pip
# RUN pip install flask psycopg2

# Expose the necessary port
EXPOSE 4000 

# Specify the command to run your application 
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"] 
