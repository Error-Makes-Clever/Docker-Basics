# Step 1: Start from base image
FROM python:3.9

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files to container
COPY . /app

# Step 4: Install dependencies
RUN pip install -r requirements.txt

# Step 5: Expose port
EXPOSE 5000

# Step 6: Define startup command
CMD ["python", "./app.py"]