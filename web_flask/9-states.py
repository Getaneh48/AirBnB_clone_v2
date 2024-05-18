#!/usr/bin/python3
"""
a script that starts a Flask web application and displays
all cities by state
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(arg=None):
    """close the session"""
    storage.close()


@app.route('/states')
def states():
    """lists cities by state"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states, s_id=None)


@app.route('/states/<id>')
def state_by_id(id):
    """get state by an id"""
    found_state = None
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)
    for state in states:
        if state.id == id:
            found_state = state
            break
    return render_template('9-states.html', state=found_state, s_id=id)


if __name__ == '__main__':
    """run the flask app"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
