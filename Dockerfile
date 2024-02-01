# Use the official MySQL image as the base image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=mysecretpassword

# Expose MySQL port
EXPOSE 3306