FROM python:3

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Create a directory for the application
WORKDIR /app

# Copy the Python script and the SQLite database file
COPY script.py /app/
COPY example.db /app/

# Run the Python script
CMD ["python", "script.py"]
