# We will be deploying to our Heroku account.

# https://dashboard.heroku.com/apps

# Account creds:
# Email: jpperaltac@gmail.com
# Password: K@wasakizx6r!

# Download Heroku toolbet -> allows you to communicate with your heroky server through your command line.
# https://devcenter.heroku.com/articles/heroku-cli#download-and-install
# Pretty much, we install the Heroku CLI by running in our Mac:
# brew tap heroku/brew && brew install heroku

# Then, open a terminal where we created our virtual environment project directory:
# /Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Fourth Application - Personal Website with Python and Flask./Mysite-VirtualEnvironment

# Run:

# heroku login -> enter your credentials from your Heroku account (shown above)

# Now we can send commands to Heroku.

# Create app - name it flask-app-udemy.

# heroku create flask-app-udemy

# List your apps:
# heroku apps

# Now open your app from the browser using this structure:
# <app-name>.herokuapp.com

# flask-app-udemy.herokuapp.com -> this will show just a custom/default heroku page. we need to upload our Flash application of course.

# For uploading files, we will use Git. First, we will create 3 files for Heroku to read:
# (1) requirements.txt -> a list of dependencies for running your python application. It tells Heroku servers to install those dependecies for us.
# (2) Procfile -> With no extension. Specifies the web server to use for running our application, as well as our application to be ran.
# (3) runtime.txt -> The python version that we want Heroku to run our app with.

# virtual/bin/pip3 freeze -> will list dependencies/libraries installed in our Virtual Python Folder Environment.
# virtual/bin/pip3 install gunicorn -> we need to install this library, as it is an http server. Heroku needs this to run our web application.
# virtual/bin/pip3 freeze -> gunicorn should be installed

# virtual/bin/pip3 freeze > requirements.txt -> Now that we have the necessary libraries within our Virtual environment to run our application, we will put them into 
# the requirements.txt file, which we will upload to the Heroku app.

# For the Procfile, put:

# web: gunicorn Flask_app:app -> tells Heroku which web server to use, for running our application. In this case, gunicorn. Also, point to our Application file (Flask_app.py), and then
# 'app' which is the name of the variable holding the Flask instance (Remember we initialize this variable in Flask_app.py as "app=Flask(__name__)")

# For runtime.txt, put:
# python-3.9.5 

# For knowing which version to select, just check the Heroku documentation on the supported python versions: https://devcenter.heroku.com/articles/python-runtimes

# Now, let's create a Git repository inside the virtual environment directory (Mysite-VirtualEnvironment):
# git init
# git add . -> we will add all our files to our git repo.
# git commit -m "My First Heroku App"

# Sets the Heroku remote github repo for our app. Also the Heroku app that will be receiving the files we will be pushing
# heroku git:remote --app flask-app-udemy

# Push the changes
# git push heroku master -> put changes to heroku. This will create the application in Heroku and install all the libraries.

# And finally, open the Heroku app:
# heroku open 

# Or you could just browse to flask-app-udemy.herokuapp.com

# heroku info -> shows info related to your app in git and heroku.




