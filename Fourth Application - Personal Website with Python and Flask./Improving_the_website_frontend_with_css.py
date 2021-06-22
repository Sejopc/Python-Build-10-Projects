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


"""
NOTE:
All CSS, Scripts and Image files go into the static folder of the current working
directory. Example, we if add .css files, they need to go into the:
static > css > main.css 

Then we link the files from the HTML pages. In this case, we link it from the
layout.html
"""