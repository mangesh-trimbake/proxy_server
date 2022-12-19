from flask import Flask
from requests import get

app = Flask('__main__')
SITE_NAME = 'https://google.com/'
SITE_NAME = 'https://www.1mg.com/'
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

app.run(host='0.0.0.0', port=8080)
