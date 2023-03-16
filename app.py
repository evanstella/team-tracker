from flask import Flask, render_template, make_response, send_from_directory

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/post_worker.js')
def post_worker():
    response=make_response(send_from_directory('static','post_worker.js'))
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'
    return response

# @app.route('/push',methods = ['POST'])
# def post_location()

if __name__ == "__main__":
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))