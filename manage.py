from istart_app import create_app, db
from config import Config
from istart_app.models.trip import TripModel

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {"app":app, "db":db, "tripModel":TripModel}