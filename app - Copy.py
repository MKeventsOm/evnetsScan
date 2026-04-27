from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inkflow-v3-secret'

# Initialize SocketIO with gevent for Railway
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

# ── ROUTES ─────────────────────────────────────────────
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

# ── SOCKET EVENTS ───────────────────────────────────────
@socketio.on('stroke')
def handle_stroke(data):
    emit('stroke', data, broadcast=True, include_self=False)

@socketio.on('clear')
def handle_clear(data=None):
    emit('clear', data or {}, broadcast=True, include_self=False)

@socketio.on('welcome_trigger')
def handle_welcome_trigger():
    emit('welcome_trigger', broadcast=True, include_self=False)

if __name__ == '__main__':
    # Local fallback
    socketio.run(app, host='0.0.0.0', port=5000)