from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


# @app.route('/push',methods = ['POST'])
# def post_location()