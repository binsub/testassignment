import logging

from flask.views import MethodView
from flask import jsonify, request
from marshmallow import ValidationError

from ..models.trip import TripModel
from ..schemas.trip_schema import TripSchema

trip_schema = TripSchema()
trip_list_schema = TripSchema(many=True)

ITEM_NOT_FOUND = "Item not found."
ITEM_DELETED = 'Item delete.'

class Trip(MethodView):
    def get(self, trip_code):
        if trip_code:
            trip = TripModel.find_by_trip_code(trip_code)
            if trip:
                return jsonify(data=trip_schema.dump(trip))

            return jsonify(message=ITEM_NOT_FOUND), 404

        return jsonify(trip_list_schema.dump(TripModel.query.all()))

    def post(self):
        trip_json = request.get_json()
       
        if 'trip_code' in trip_json:
            project = TripModel.find_by_trip_code(trip_json['trip_code'])

            if project:
                raise ValidationError({'message':'trip already exists'})

        project = trip_schema.load(trip_json)
        project.save_to_db()
        return jsonify(message='trip created.'),201

    def delete(self, trip_code):
        trip = TripModel.find_by_trip_code(trip_code)
        if trip:
            trip.delete_from_db()
            return '', 204

        return jsonify(message=ITEM_NOT_FOUND), 404
        return '', 204

    def put(self, trip_code):
        trip = TripModel.find_by_trip_code(trip_code)
        
        if trip:
            trip_json = request.get_json()
            trip_schema.load(trip_json)

            trip.trip_code = trip_json['trip_code']
            trip.payment =  trip_json['payment']
            trip.pick_up_location = trip_json['pick_up_location']
            trip.drop_off_location = trip_json['drop_off_location']
            trip.driver_name = trip_json['driver_name']
            trip.customer_name = trip_json['customer_name']
            trip.car_number = trip_json['car_number']

            logging.error(trip)

            trip.save_to_db()
            return '', 204

        return jsonify(message=ITEM_NOT_FOUND), 404