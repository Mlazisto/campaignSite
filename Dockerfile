# Use the official Python image as the base image
FROM python:3


# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files to the working directory
COPY . /app/

# Expose the port your Django app will run on (change this to your Django project's actual port)
EXPOSE 8000

# Run the Django development server (change this command based on your Django project)
CMD ["python", "manage.py", "runserver"]
