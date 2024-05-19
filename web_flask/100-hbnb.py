#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, State, Amenity, City, Place

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(arg=None):
    """close the session"""
    storage.close()

@app.route('/hbnb')
def hbnb():

    """lists cities by state"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)

    all_amenities = storage.all(Amenity)
    amenities = sorted(all_amenities.values(), key=lambda amenity: amenity.name)

    all_places = storage.all(Place)
    places = sorted(all_places.values(), key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

@app.route('/hbnb_filters')
def hbnb_filters():
    """lists cities by state"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)

    all_amenities = storage.all(Amenity)
    amenities = sorted(all_amenities.values(), key=lambda amenity: amenity.name)
    
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)



if __name__ == '__main__':
    """run the flask app"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
