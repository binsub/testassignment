from .. import db, ma

class TripModel(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    trip_code = db.Column(db.String(255), nullable=False)
    payment = db.Column(db.Float, nullable=False)
    pick_up_location = db.Column(db.String(255), nullable=False)
    drop_off_location = db.Column(db.String(255), nullable=False)
    driver_name = db.Column(db.String(255), nullable=False)
    customer_name = db.Column(db.String(255), nullable=False)
    car_number = db.Column(db.String(255), nullable=False)

    @classmethod
    def find_by_trip_code(cls, trip_code: str) -> "TripModel":
        return cls.query.filter_by(trip_code=trip_code).first()

    @classmethod
    def find_by_id(cls, id: int) -> "TripModel":
        return cls.query.filter_by(id=id).first()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

