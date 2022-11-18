from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/caraccident')
def accident():
    return render_template('caraccident.html')


@app.route('/time')
def time():
    return render_template('time.html')


@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')


if __name__ == '__main__':
    app.run(debug=True)
