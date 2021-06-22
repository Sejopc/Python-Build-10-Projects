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

    NOTE: This is a comment that goes on lines 18 and 19 from layout.html page,
    however no comments are allowed there as that is the parent template (child templates 
    don't support comments neither). So, putting them here.

    Line 18: Template inheritance. It will run/execute whatever is between "{%block content%} tags on the .html files it is inherited."
    layout.html is the parent template. Child templates are: /home.html and /about.html pages
    The child templates are the ones who will fill the block template above ( {%block content%} )
    Line 19: Needed to specify where the templates finish.

"""