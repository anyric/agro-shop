# Agroshop
## Description
This repo contains a Python Flask Web Application website for local company dealing in agricultural inputs and advisory services. The company sales all agricultural inputs and tools as well as provide advisory services to farmers through radio talk shows and telephone call including onsite and face to face.

## Setup
### Dependencies
* [Python >= 3.6](https://www.python.org/) - popular general-purpose scripting language suited for web development
* [Flask 1.1.2](http://flask.palletsprojects.com/en/1.1.x/) - A web application framework for Python

### Getting Started
Setting up project in development environment
* Ensure Python >=3.6 is installed by running:
```
python --version
```
* Ensure pipenv is installed or you can follow the intallation from [PIPENV](https://docs.pipenv.org/)
* Create a folder for the project by running:
```
mkdir myprojectfoldername
```
* cd in to `myprojectfoldername`
* Create a virtualenv using pipenv by running:
```
pipenv shell
```
* Clone the project repo by running:
```
git clone https://github.com/anyric/agro-shop.git
```

### Running the application
* Export the .env file by running 
```
. .env or source .env
```
* Inside the project root folder i.e agro-shop/, run the command below in your console
```
flask run
```
* Navigate to `http://127.0.0.1:5000/`

## Developer and Maintainer
* Anyama Richard