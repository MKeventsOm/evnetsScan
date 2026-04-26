from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inkflow-v3-secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')


# ── PAGES ──────────────────────────────────────────────

@app.route('/')
def index():
    """Main menu — two buttons: Sign / Welcome"""
    return render_template('index.html')


# SIGN mode
@app.route('/ipad')
def ipad():
    """iPad: horizontal signature pad"""
    return render_template('ipad.html')

@app.route('/screen')
def screen_sign():
    """Screen: live signature display"""
    return render_template('screen_sign.html')


# WELCOME mode
@app.route('/ipad-welcome')
def ipad_welcome():
    """iPad: welcome trigger controller"""
    return render_template('ipad_welcome.html')

@app.route('/screen-welcome')
def screen_welcome():
    """Screen: plays video then shows photo"""
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
    """iPad pressed Welcome button → broadcast to all screens"""
    emit('welcome_trigger', broadcast=True, include_self=False)


# ── RUN ─────────────────────────────────────────────────

if __name__ == '__main__':
    print("\n" + "="*55)
    print("  InkFlow v3 — Running!")
    print("="*55)
    print("  Main Menu         : http://127.0.0.1:5000")
    print("")
    print("  ── SIGN MODE ──")
    print("  iPad (sign pad)   : http://127.0.0.1:5000/ipad")
    print("  Screen (live)     : http://127.0.0.1:5000/screen")
    print("")
    print("  ── WELCOME MODE ──")
    print("  iPad (controller) : http://127.0.0.1:5000/ipad-welcome")
    print("  Screen (display)  : http://127.0.0.1:5000/screen-welcome")
    print("="*55 + "\n")
    socketio.run(app, debug=False, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
