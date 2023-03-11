from flask import Flask, request, render_template, session
from flask_cors import CORS, cross_origin
import urllib
import json
from scrap import get_data


API_KEY = "How8Mc7ey9amKdoS7kJDeyaMXUtIEQS8"


app = Flask(__name__, template_folder='templates')
app.secret_key = 'cjksfhkewjfdlwkjdfw35k3jblk'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def get_link_info(api_key, url):
    encoded_url = urllib.parse.quote(url, safe='')
    api_url = "https://ipqualityscore.com/api/json/url/"
    data = urllib.request.urlopen(api_url + api_key + "/" + encoded_url)
    data = data.read()
    data = json.loads(data)
    return data


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/get-details', methods=['POST'])
@cross_origin()
def get_details():
    if request.method == "POST":
        url = request.form['url']
        data = get_link_info(API_KEY, url)
        session['url'] = url
    return render_template("info.html", data=data)

@app.route('/show-data')
def show_data():
    url = session['url']
    data = get_data(url).split('\n')
    return render_template("site_data.html", data=data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
