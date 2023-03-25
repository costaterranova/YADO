from flask import Flask, render_template, session
from generator import activity_finder


app = Flask(__name__) # holds the name of the current Python module
app.secret_key = 'mysecretkey'


@app.route('/') 
    # This function fires when someone hits Base ("/") url
    # You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
def hello():
    return render_template('index.html')

@app.route('/yado') 
def hello2():
    activity, time = activity_finder()

    return render_template('generated_activity.html', activity=activity, time=time)
if __name__ == '__main__':
   app.run()