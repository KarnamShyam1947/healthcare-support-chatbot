# Use the official slim Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies that are required (if you have a requirements.txt file)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (Optional)
EXPOSE 8080

# Command to run your bot
CMD ["python", "telegram_bot.py"]
