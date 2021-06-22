# We will be using Heroku Cloud for deploying our applications in the cloud.

# Before uploading our app to the cloud, we need to create a virtual environment.

# Create a folder called: Mysite-VirtualEnvironment.

# Change to that folder (cd Mysite-VirtualEnvironment). Copy the folder "static" and folder "Templates" from the previous directory to this new virtual environment directory (Mysite-VirtualEnvironment).
# Additionally, copy the Flash python application (Flask_app.py) to this virtual env folder as well

# Run:
# python3 -m venv virtual -> will create a "virtual" folder with an isolated python environment.
# cd virtual/
# bin/python3 -> just for texting python3 works. Then exit using: exit().
# bin/pip3 install flask -> install flask library in our virtual env.
# Run it (from  MySite-VirtualEnvironment folder):

# virtual/bin/python3 Flash_app.py


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Decorator
def home2():
    return render_template("home2.html") # Here we changed it from home.html to home2.html file since we will be using it as a child template.


@app.route('/about/') # Decorator
def about2():
    return render_template("about2.html") # Here we changed it from about.html to about2.html file since we will be using it as a child template.

if __name__ == "__main__":
    app.run(debug=True)
