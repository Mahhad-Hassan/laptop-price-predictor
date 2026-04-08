# Base Image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy full project
COPY . .

# Expose Port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]