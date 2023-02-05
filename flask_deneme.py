from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    numbers = [1,2,3,4,5]
    
    return render_template("index.html",numbers=numbers)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)