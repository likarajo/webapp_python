# Python Web Application

A python web application with REST API built using Flask deployed to Heroku.

* Receives a name
* Returns a welcome message

## Create and activate a virtual environment

```
python3 -m venv venv/
source venv/bin/activate
```

## Install Dependencies

Developed in **Python 3.7.0**

* **Flask** 1.1.1: To build the app
* **Gunicorn** 20.0.4: For the server

`pip install -r requirements.txt`

## Build and run the application locally

* app.py

```
$ python3 app.py
```

* application runs locally in http://127.0.0.1:5000/

```
Welcome to the server
```

* POST: http://127.0.0.1:5000/getmsg/?name=Raj

```
{"MESSAGE":"Welcome Raj!"}
```

## Deploy the Application

### *Heroku*

* It is a cloud platform as a service (PaaS)
* Supports several languages - Ruby, Java, Node.js, Scala, Clojure, Python, PHP, and Go.
* Create a Heroku account: https://signup.heroku.com/
* Install Herock CLI: https://devcenter.heroku.com/articles/heroku-command-line `brew tap heroku/brew && brew install heroku`
* Uses the *Git* repository to deploy

### Deployment process

* Create the ***requirements.txt*** file in the project repository
  * Heroku knows the modules that are used from the this file.

* Create the ***Procfile*** in the project repository
  * Heroku knows the processes/commands needed to run the application from this file.
  * The *web* command is to start a web server for the application.

* Create a new app in Heroku
  * Choose app name
  * Choose a region for hosting

* Login to Heroku from the CLI:  

`$ heroku login -i`

* Add the project repository to the remote:  

`$ heroku git:remote -a {project-name}`

* Upload the project by pushing to Heroku:  

`$ git push heroku master`

### Testing

* The app gets deployed to https://likarajo-test.herokuapp.com/

* Goto https://likarajo-test.herokuapp.com/ to test the GET API

* Goto https://likarajo-test.herokuapp.com/getmsg/?name=Raj to test the POST API

* Goto https://likarajo-test.herokuapp.com/getmsg/?age=28 to test the POST API without the 'name' paramneter that gives ERROR

* Goto https://likarajo-test.herokuapp.com/newurl to test the GET returning 404 Not Found reponse

## Conclusion

* Python App with APIs are built using **Flask**
* The deployment has been done using **Git**
* The web hosting has been done using **Gunicorn**
* The app has been deployed in **Heroku**
