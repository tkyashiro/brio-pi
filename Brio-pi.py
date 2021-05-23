from flask import Flask, render_template, request
from json import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Top")

if __name__ == "__main__":
    # app.run(debug=True)
    #app.run(debug=False, host='192.168.0.210', port=5010)
    app.run(debug=False, host='192.168.11.52', port=5010)

