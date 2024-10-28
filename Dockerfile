FROM python:3.12-slim

WORKDIR /app


COPY . /app

# Install any required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 (the default Django development server port)
EXPOSE 8000

# Command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
