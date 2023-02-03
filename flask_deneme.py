from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    sayi = 10
    sayi2 = 20
    
    return render_template("index.html", number=sayi, number2=sayi2)

if __name__ == "__main__":
    app.run(debug=True)