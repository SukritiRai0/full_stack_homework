# Use the official Node.js LTS image as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which the app runs (default is 3000 for create-react-app)
EXPOSE 3000

# Command to run your app
CMD ["npm", "start"]