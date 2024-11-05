from flask import Flask, render_template, request
import datetime
import threading
import time
import winsound  # For playing sound on Windows

app = Flask(__name__)

alarm_time = None
alarm_thread = None
alarm_active = threading.Event()  # Use threading Event for better thread synchronization

def play_alarm():
    """Function to play alarm sound."""
    while alarm_active.is_set():
        winsound.Beep(1000, 1000)  # Frequency, Duration in milliseconds
        time.sleep(1)  # Adjust to how often the sound should repeat

@app.route('/')
def index():
    """Render the alarm clock home page."""
    return render_template('alarm.html')

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    """Set the alarm time from the user input."""
    global alarm_time, alarm_thread
    alarm_time_str = request.form.get('alarmTime')
    
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, '%H:%M').time()
    except ValueError:
        return 'Invalid time format, please use HH:MM format'

    alarm_active.set()  # Activate the alarm event
    if alarm_thread is None or not alarm_thread.is_alive():
        alarm_thread = threading.Thread(target=check_alarm)
        alarm_thread.start()

    return f'Alam set for {alarm_time_str}'

def check_alarm():
    """Check the current time against the alarm time."""
    while alarm_active.is_set():
        now = datetime.datetime.now().time()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            play_alarm()
            break  # Stop the thread when the alarm goes off
        time.sleep(10)  # Check every 10 seconds

@app.route('/stop_alarm', methods=['POST'])
def stop_alarm():
    """Stop the alarm."""
    alarm_active.clear()  # Stop the alarm thread
    return 'Alarm stopped'

if __name__ == '__main__':
    app.run(debug=True)
