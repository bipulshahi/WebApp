#pip install Flask

from flask import Flask

app = Flask(__name__)


@app.route('/my_name')
def my_name():
    return 'Bipul Kumar Shahi'


app.run()
