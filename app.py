from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inkflow-secret-2024'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
@socketio.on('start_session')
def handle_start():
    # نرسل إشارة لجميع صفحات العرض المفتوحة
    emit('start_session', broadcast=True, include_self=False)

@app.route('/')
def draw():
    return render_template('draw.html')


@app.route('/view')
def view():
    return render_template('view.html')


@socketio.on('stroke')
def handle_stroke(data):
    emit('stroke', data, broadcast=True, include_self=False)


@socketio.on('clear')
def handle_clear():
    emit('clear', broadcast=True, include_self=False)

@socketio.on('end_session')
def handle_end():
    emit('end_session', broadcast=True, include_self=False)
if __name__ == '__main__':
    print("\n" + "="*45)
    print("  ✓ InkFlow يعمل!")
    print("  لوحة الكتابة  : http://127.0.0.1:5000")
    print("  العرض المباشر : http://127.0.0.1:5000/view")
    print("="*45 + "\n")
    socketio.run(app, debug=False, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
