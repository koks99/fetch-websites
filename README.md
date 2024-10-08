# Python Program to Fetch Webpages

## Table of Contents

- [Description](#Description)
- [Setup](#Setup)
- [Usage](#Usage)
- [Misc](#Misc)

## Description
This project is a python program which helps in extracting data from a given set of webpages enclosed with Docker for making it platform-agnostic.

## Setup

### Prerequisites:

Ensure that you have the following installed before proceeding with the setup:
1. Docker and Docker Compose (OR)
2. Docker Desktop application

### Docker build:

```sudo docker-compose build```

## Usage

### Running Unit Tests
```sudo docker-compose run test```

### Running the Application
1. You can pass single or multiple URLs separated by space:
>```sudo docker-compose run web-fetcher <URL1> <URL2>```
2. To fetch metadata like the number of links and images from the website, add the --metadata flag:
>```sudo docker-compose run web-fetcher <URL1> <URL2> --metadata```
3. To create a mirror copy of the website locally, add the --mirror flag:
>```sudo docker-compose run web-fetcher <URL1> <URL2> --mirror```
4. Both flags can be used simultaneously as well.

## Misc

### Troubleshooting
- If any expected errors are thrown while building the docker image, running this command could help:
```sudo rm  ~/.docker/config.json```
- If you notice orphan containers being created, try using the `--project-name` flag in Docker Compose to avoid multiple containers for the same project.

### Future Improvements
1. Right now, the script can be used only within the project directory, we can add support to make it global in such a way the script can be run from anywhere in the system.
2. The mirror option now utilises `pywebcopy` package which is not 100% reliable. We can design and implement a custom scrapping solution to get better results for downloading the assets.