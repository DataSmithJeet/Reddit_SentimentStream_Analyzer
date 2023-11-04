# Use the official python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY reddit_data_fetcher.py /app/reddit_data_fetcher.py

# Install PRAW (Python Reddit API Wrapper) and confluent kafka
RUN pip install praw confluent-kafka

# Run reddit_data_fetcher.py when the container launches
CMD ["python", "reddit_data_fetcher.py"]