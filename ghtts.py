from googlehomepush import GoogleHome
from flask import Flask, request
app = Flask(__name__)


'''
Thanks to this project for doing the actual work:
https://pypi.org/project/googlehomepush/

Example Curl:
curl -G http://host_this_is_running_on:8069/say/ --data-urlencode "saywhat=Lou Reed is great!"
'''


@app.route('/say/')
def speak():
    '''
    This takes text supplied as a param in the URL and speaks it, eg:
    http://host_this_is_running_on:8069/say?saywhat=Hello World
    '''
    saywhat = request.args.get('saywhat')
    GoogleHome("Downstairs").say(saywhat, lang='en-GB')
    return 'I said ' + saywhat


@app.route('/')
def upcheck():
    '''
    This allows Monit or PRTG to do it's HTTP check to see if the host is up.
    '''
    return "GHTTS is Up!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8069")
