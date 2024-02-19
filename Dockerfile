# Use Alpine Linux as a base image
FROM alpine:latest

# Install Python
RUN apk --no-cache add python3

# Set the working directory
WORKDIR /home

# Copy the Python script into the container
COPY script.py /home/script.py

# Set the default command to run the script
CMD ["python3", "/home/script.py"]
