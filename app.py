from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hostname():
    return socket.gethostname()


@app.route('/terminate')
def terminate():
    import os
    os.system("killall -KILL python")
    return
