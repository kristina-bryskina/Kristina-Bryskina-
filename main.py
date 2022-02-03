from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/katolog')
def katolog():
    return render_template("katolog.html")

@app.route('/inf')
def inf():
    return render_template("inf.html")

@app.route('/sale')
def sale():
    return render_template("sale.html")

if __name__ == '__main__':
    app.run(debug=True)