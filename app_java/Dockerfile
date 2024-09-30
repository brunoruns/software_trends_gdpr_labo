# Use the official OpenJDK image from the Docker Hub
FROM openjdk:11-jre-slim

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/demo-0.0.1-SNAPSHOT.jar .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Spring Boot application
CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]
