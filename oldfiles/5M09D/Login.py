from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABSE_URL'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    e


user = []

@app.route('/', methods=['GET'])
def register():
    user_id = request.json["id"]
    user_pw = request.json["pw"]
    register_type_error = Response("Be not a str.", 403)
    register_error = Response("Already registered ID",409)
    register_success = Response("Register Success : " + user_id, 200)

    if type(user_id) == str \
            and type(user_pw) == str:
        for register in user:
            if register['id'] == user_id:
                return register_error
        else:
            user.append({
                'id': user_id,
                'pw': user_pw
            })
            print("Register : ", user_id)
            return register_success
    else:
        return register_type_error


@app.route('/login', methods=['POST'])
def login():
    login_id = request.json["id"]
    login_pw = request.json["pw"]
    login_success = Response("Hello "+login_id, 200)
    login_failed = Response("Login failed", 401)

    for login in user:
        if login['id'] == login_id \
                and login['pw'] == login_pw:
            print("Login Success")
            return login_success
    return login_failed

if __name__ == '__main__':
    app.run(debug=True)