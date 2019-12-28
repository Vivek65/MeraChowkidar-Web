import flask
from flask import jsonify, request, Flask

import mc_base_file as base_file

app = Flask(__name__)


@app.route('/api/v1/resources/state', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'lat' in request.args:
        lat = float(request.args['lat'])

    if 'lng' in request.args:
        lng = float(request.args['lng'])

    # Create an empty list for our results
    results = base_file.return_location_data(lng, lat)

    if results is None:
        return "Invalid Lat long"
    return "Cloud se aa rha hai"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
