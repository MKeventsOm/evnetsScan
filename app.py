from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'inkflow-secret-2024'
socketio = SocketIO(app, cors_allowed_origins="*")
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
    port = int(os.environ.get("PORT", 5000))
    # Use socketio.run for better WebSocket support
    socketio.run(app, host='0.0.0.0', port=port)
