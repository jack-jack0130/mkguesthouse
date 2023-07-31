from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():

    return render_template('home.html' )

@app.route('/rooms')
def rooms():

    return render_template('rooms.html' )

@app.route('/map')
def map():

    return render_template('map.html' )

@app.route('/book')
def book():

    return render_template('book.html' )


@app.route('/attracions')
def attractions():

    return render_template('attractions.html' )


if __name__ == '__main__':
    app.run(debug=True)