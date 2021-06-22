from flask import Flask

app = Flask(__name__)


@app.route('/about/') # Decorator
def about():
    return "About section here!"

@app.route('/') # Decorator
def home():
    return "Home page here!"

if __name__ == "__main__":
    app.run(debug=True)

  

