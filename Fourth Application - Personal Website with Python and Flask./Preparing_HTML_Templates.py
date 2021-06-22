from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Decorator
def home():
    return render_template("home.html") # For this to work, we need to create a "Templates" folder on this same file directory level.

@app.route('/about/') # Decorator
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

  