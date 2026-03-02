import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I'm waving at {name}"

# @app.route('/', methods=['GET'])
# def index():
#     name = request.args['name']
#     return f"Hello, {name}!"

# @app.route('/test_post', methods=['POST'])
# def test_post():
#     dob = request.form['dob']
    # return f"you dob is: {dob}"

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))