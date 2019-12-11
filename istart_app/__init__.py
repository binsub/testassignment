from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_object):
    app = Flask(__name__)

    app.config.from_object(config_object)

    from .routes.trip import Trip

    trip_view = Trip.as_view('trip_api')

    # Registering endpoint
    app.add_url_rule('/api/v1/trip', methods=['POST'], view_func=trip_view)
    app.add_url_rule('/api/v1/trip', methods=['GET'], defaults={'trip_code': None}, view_func=trip_view)
    app.add_url_rule('/api/v1/trip/<trip_code>', methods=['GET', 'PUT', 'DELETE'], view_func=trip_view)

    # initializing orm and serializer
    db.init_app(app)
    ma.init_app(app)

    return app



