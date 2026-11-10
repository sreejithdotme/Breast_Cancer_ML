
# 1. Use an official Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependency list
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project files into the container
COPY app.py .
COPY models/ ./models/

# 6. Expose Streamlit's default port
EXPOSE 8501

# 7. Start the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
