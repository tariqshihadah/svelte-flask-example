# Server features
from flask import Flask, request, send_from_directory, Response, jsonify
from logging import FileHandler, WARNING

# Utilities
import random, json

# Data IO
import ops
from ops.load_data import _load_from_path, _load_sample_data
from ops.globals import _loaded_data


#
# DEFINE APPLICATION
#

app = Flask(__name__)
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


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

@app.route("/data/push/<path:name>", methods=['POST'])
def data_push(name):
    # Retrieve data from POST
    data = json.loads(request.json)
    # Log to loaded data variable
    _loaded_data[name] = data
    # Update console
    print(f"Loaded data: {name}")
    return {}, 200

@app.route("/data/pull/<path:name>", methods=['POST'])
def data_pull(name):
    # Grab data from memory
    try:
        response = _loaded_data[name].to_json()
        status = 200
    except KeyError:
        response = {
            'message': 'data unavailable from memory',
            'name': name,
        }
        status = 404
    # Prepare data
    return response, status

#
# VISUALIZATION ENDPOINTS
#

app.route("/viz/map")


#
# TESTING FEATURES
#

_loaded_data['us-states.json'] = _load_from_path(r"C:\Users\tariq\Downloads\us-states.json")
print(_loaded_data)


#
# RUN APPLICATION
#

if __name__ == "__main__":
    app.run(debug=True)
