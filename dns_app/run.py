from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/time')
def time():
    current_time = str(datetime.now())
    return current_time

app.run(host='0.0.0.0',
        port=8080,
        debug=False)