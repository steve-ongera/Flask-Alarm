# Flask Alarm Clock
This project is a simple Flask-based alarm clock application. It allows users to set an alarm time, which will trigger an alarm sound when the time is reached. The application runs on a web server and interacts with users via a user-friendly web interface.

## Features
- Set Alarm: Allows users to set a time for the alarm.
- Play Alarm: When the set alarm time is reached, a beep sound will be played repeatedly.
- Stop Alarm: A button to stop the alarm once it rings.
- Web Interface: Simple and interactive web interface using Flask and HTML templates.
## Demo
You can view the demo of this project by running it locally.

## Installation
To run this Flask alarm clock app on your local machine:

1. Clone the repository or download the project files

git clone https://github.com/steve-ongera/flask-alarm-clock.git
2. Navigate to the project folder

``cd flask-alarm-clock``
3. Install dependencies
Make sure you have Python and pip installed. Then install Flask and any other required dependencies:

``pip install Flask``
4. Run the Flask application
Execute the following command to start the Flask development server:


``python app.py``
Your Flask app will now be running locally. Open a web browser and go to:

http://127.0.0.1:5000/
You should see the alarm clock interface.

## How It Works
Set the Alarm:

Use the web interface to input the desired alarm time in the format HH:MM (24-hour format).
Press the "Set Alarm" button to save the alarm time.
Alarm Sound:

When the current time matches the alarm time, a beep sound will play repeatedly.
The sound is generated using the winsound.Beep() function on Windows systems.
Stop the Alarm:

Once the alarm is triggered, the user can press the "Stop Alarm" button to stop the sound.
The alarm thread will be stopped, and the sound will stop immediately.
Project Structure
perl

``flask-alarm-clock/
├── app.py                  # Main Flask application file
├── templates/
│   ├── alarm.html          # HTML file for the alarm clock interface
├── static/
│   ├── css/                # CSS folder (if any custom styles)
│   ├── js/                 # JavaScript folder (if any custom JS)
└── requirements.txt       `` # Python dependencies (optional)


## Explanation of Files

- app.py: Contains the Flask application code, including routes and logic for setting, checking, and stopping the alarm.
- alarm.html: The HTML template that renders the alarm clock interface, allowing the user to input alarm time and control the alarm.
- static/: If you have any custom CSS or JavaScript files, they would go here (optional).
- templates/: Contains the HTML templates used by Flask for rendering the pages.

## How to Use
- Set Alarm
- Navigate to the home page of the alarm clock app.
- Enter the desired alarm time in the HH:MM format in the text box.
- Press Set Alarm to set the alarm.
- Stop Alarm
- Once the alarm goes off, press the Stop Alarm button to stop the sound.

## Dependencies
This project requires Python 3.x and the following libraries:

## Flask
winsound (only for Windows systems)
To install the required dependencies, run:


pip install Flask
If you're using a Windows machine, winsound is already included in Python's standard library, so you don't need to install it separately.

## Customization
You can customize the following aspects:

Alarm Sound
The alarm sound is played using the winsound.Beep() function. You can change the frequency or duration of the beep sound to suit your preferences. For example:


winsound.Beep(1000, 1000)  # Frequency (Hz), Duration (ms)


## Modify Alarm Time Format
The current time format expects the user to enter the alarm time in the HH:MM format. You can adjust this format in the code if you want a different time format.

## Add More Features
- Repeat Alarm: You can modify the code to repeat the alarm after a certain period if needed.
- Alarm Sounds: You can use external audio files for the alarm sound instead of winsound.Beep() by using a library like pygame or playsound.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Contributions are welcome!

##  Reporting Issues
If you encounter any bugs or issues with the functionality of the app, please open an issue on the GitHub repository, and we will address it as soon as possible.

## Feature Requests
If you have ideas for new features, feel free to submit a feature request.

## License
This project is open-source and available under the MIT License.

This README.md file provides detailed instructions for setting up, using, and customizing your Flask-based alarm clock app. Make sure to replace the placeholder links with actual ones if you host the repository online.