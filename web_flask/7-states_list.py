#!/usr/bin/python3
"""
a script that starts a Flask web application and displays
all states
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(arg=None):
    """close the session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """lists all state"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """main function runs flask app"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
