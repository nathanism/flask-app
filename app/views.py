from app import app

# Import controllers to call
from app.controllers import home

app.route('/')(home.index)
