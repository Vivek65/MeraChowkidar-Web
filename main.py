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


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
