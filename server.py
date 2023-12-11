from flask import Flask, send_from_directory
import random
import ops
from ops.load_data import _load_from_path, _load_sample_data


#
# DEFINE APPLICATION
#

app = Flask(__name__)


#
# WEB PAGE ROUTES
#

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


#
# DATA LOADING ENDPOINTS
#

@app.route("/load_from_path/<path:path>")
def load_from_path(path):
    return _load_from_path(path).to_json()

@app.route("/load_sample_data/<path:label>")
def load_sample_data(label):
    return _load_sample_data(label).to_json()


#
# VISUALIZATION ENDPOINTS
#

app.route("/viz/map")


#
# RUN APPLICATION
#

if __name__ == "__main__":
    app.run(debug=True)
