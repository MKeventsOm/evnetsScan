import eventlet
eventlet.monkey_patch()

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'inkflow-v3-secret')

# async_mode must be 'eventlet'

# ... rest of your routes and events ...

# Make sure it's eventlet here
socketio = SocketIO(
    app, 
    cors_allowed_origins="*", 
    async_mode='eventlet',
    engineio_logger=False, # Set to True if you need to see logs in Railway
    always_connect=True
)# -- PAGES --
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ipad')
def ipad():
    return render_template('ipad.html')

@app.route('/screen')
def screen_sign():
    return render_template('screen_sign.html')

@app.route('/ipad-welcome')
def ipad_welcome():
    return render_template('ipad_welcome.html')

@app.route('/screen-welcome')
def screen_welcome():
    return render_template('screen_welcome.html')

@socketio.on('stroke')
def handle_stroke(data):
    # 'broadcast=True' sends it to every connected client EXCEPT the sender
    # because we set include_self=False
    emit('stroke', data, broadcast=True, include_self=False)

@socketio.on('clear')
def handle_clear(data=None):
    emit('clear', data or {'type': 'sign'}, broadcast=True, include_self=False)
    
@socketio.on('welcome_trigger')
def handle_welcome_trigger():
    emit('welcome_trigger', broadcast=True, include_self=False)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)