# Use the base image of Ubuntu 20.04
FROM ubuntu:20.04

# Update the package list and install necessary dependencies
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /main

# Copy application files (if any) into the container
COPY ./copy_dir /main

# Specify the command to be executed when the container starts
CMD ["bash"]