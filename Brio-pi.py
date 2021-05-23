from flask import Flask, render_template, request, Response
from Camera import Camera
from json import *
import signal
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Top")

@app.route('/snapshot')
def shapshot():
    return render_template('snapshot.html', title="Snapshot")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def sigint_handler(signal, frame):
    app.logger.debug("Closing")
    # p.stop()
    # q.stop()
    app.logger.debug("Closed")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)

    # app.run(debug=True)
    #app.run(debug=False, host='192.168.0.210', port=5010)
    app.run(debug=False, host='192.168.11.52', port=5010)

