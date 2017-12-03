from flask import Flask, jsonify, abort, request
from firebase import firebase
import requests

app = Flask(__name__)
firebase = firebase.FirebaseApplication(
    'https://travatar-c5cfb.firebaseio.com', None)
CLOUD_URL = "https://us-central1-travatar-c5cfb.cloudfunctions.net"


@app.route('/users/<string:user_id>')
def users(user_id):
    profile = firebase.get('/users/{}'.format(user_id), "public")
    return jsonify(profile)


@app.route('/users')
def users_by_email():
    # TODO: single network call
    email = request.args.get("email")
    if email:
        r = requests.get(CLOUD_URL + "/user_by_email", params={"email": email})
        if r.status_code != 200:
            abort(404)
        user_id = r.text

    profile = firebase.get('/users/{}'.format(user_id), "public")
    return jsonify(profile)


@app.route('/test')
def test():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
