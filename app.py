from flask import Flask
from flask import request
import socket

app = Flask(__name__)


@app.route('/about')
def about():
    return """ <center><b><p style="font-family:Tahoma;color:red;font-size: 15px">This WebApp was made by David Gitman<br/>
               The following Flask app will get a Docker Container Host name and Host IP.<br/>
               In Order to run this flask app in a stand alone mode run app.py using 'python -m flask run' command.<br/>
               </center></b></p>"""


@app.route('/')
def readme():
    return """ <center><b><p style="font-family:Tahoma;color:red;font-size: 15px">Welcome to my first flask app!<br/>
               You can check the host name and IP by going into /host<br/>
               In order to stop the server you can shut it down by entering /stop<br/>
               For more info head into /about</center><br/></b></p>"""


@app.route("/host")
def hostname():
    host1 = socket.gethostname()
    host2 = socket.gethostbyname(host1)
    return " <center><b><p style='font-family:Tahoma;color:red;font-size: 15px'>Host Name:  </b>" + host1 + "<center><b><p style='font-family:Tahoma;color:red;font-size: 15px'>Host IP:  </b>" + host2


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/stop')
def shutdown():
    shutdown_server()
    return "Server shutting down..."

