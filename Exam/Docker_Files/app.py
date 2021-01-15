from flask import Flask
from flask import render_template
import ipinfo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ipinfo')
def ip():
    access_token = '65a844d5bc532e'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    return details.all

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
