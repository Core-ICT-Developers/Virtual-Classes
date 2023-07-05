#pip install flask
#pip install flask-sqlalchemy
from flask import Flask



app = Flask(__name__)


@app.route('/')
def index():
  return "Simple index page"


#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")