from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/count')
def count():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/')
def hello():
    return "Hello! You're being served by: "+os.uname()[1]

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
