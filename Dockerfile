# Use the bitnami/python:3.11 image as the base image
FROM bitnami/python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy your project files to the container
COPY . /app

# Create a virtual environment called "venv"
RUN python -m venv vtenv

# Activate the virtual environment
RUN source vtenv/bin/activate

# Install the Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 80
EXPOSE 80

# Command to run the FastAPI app with Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
