from flask import Flask, request, render_template
from db import db
from controllers import controller
import json
from flask_cors import CORS

app = Flask(__name__)
api = db
CORS(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    return controller.insert_user(username, email, password)


@app.route('/users')
def users():
    users = controller.get_all_users_json()
    return users



@app.route("/populate", methods = ['POST'])
def populate():
  return controller.populate(int(request.args.get('n')))

if __name__ == '__main__':
  app.run(debug=True, port=8000)
