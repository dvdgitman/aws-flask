from flask import Flask
from flask import request
import socket

app = Flask(__name__)


@app.route("/host")
def hostname():
    return socket.gethostname()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/stop')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
