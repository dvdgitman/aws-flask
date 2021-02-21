from flask import Flask
from flask import request
import socket

app = Flask(__name__)


@app.route('/')
def readme():
    return """ <center><b><p style="font-family:Tahoma"; color:red; font-size: 20px>Welcome to my first flask app!<br/>
               You can check the host name and IP by going into /host<br/>
               In order to stop the server you can shut it down by entering /stop</center></b></p>"""


@app.route("/host")
def hostname():
    host = socket.gethostname()
    host2 = socket.gethostbyname(host)
    return " <center><b><p style='font-family:Tahoma';>Host Name:  </b>" + host + "<center><b><p style='font-family:Tahoma';>Host IP:  </b>" + host2




def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/stop')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
