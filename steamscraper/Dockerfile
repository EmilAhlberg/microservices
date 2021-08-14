# official Python 3 Docker image.
FROM python:3

# working directory = /usr/src/app.
WORKDIR /usr/src/app

# cpy requirement list to the container at the WORKDIR.
COPY requirements.txt ./

# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# cpy source code to the container at WORKDIR.
COPY . .

# run crawler on launch
CMD [ "python3", "./run_scraper.py" ]
