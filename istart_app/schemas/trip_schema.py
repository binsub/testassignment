from .. import db, ma
from ..models.trip import TripModel


class TripSchema(ma.ModelSchema):
    class Meta:
        model = TripModel
        dump_only = (id, )