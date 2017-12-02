from flask import Flask, jsonify
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://travatar-c5cfb.firebaseio.com', None)

@app.route('/users/<string:user_id>')
def user(user_id):
    profile = firebase.get('/users/{}'.format(user_id), "public")
    return jsonify(profile)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    