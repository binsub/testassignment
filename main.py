from istart_app import create_app
from flask_basicauth import BasicAuth
from marshmallow import ValidationError
from flask import jsonify
from config import Config

app = create_app(Config)
basicauth = BasicAuth(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)