# Use an official Python runtime as an image
FROM python:3.8

# creates a directory with this name if it doesn’t exist
WORKDIR /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python"]
CMD ["app.py"]
