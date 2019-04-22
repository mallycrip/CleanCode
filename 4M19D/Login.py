from flask import Flask, request, Response

app = Flask(__name__)

user = []

@app.route('/', methods=['POST'])
def register():
    id = request.json["id"]
    pw = request.json["pw"]

    user.append({
        'id':id,
        'pw':pw
    })

    response = Response("Register Success | id : "+id)
    print("Register Success", id)
    print(user)
    return response

@app.route('/login', methods=['POST'])
def login():
    login_id = request.json["id"]
    login_pw = request.json["pw"]

    for a in user:
        print(a)
        if a['id'] == login_id:
            if a['pw'] == login_pw:
                print("Login Success")
                return "LOGIN SUCCESS"
            else:
                return "Check your pw."
    return "Check your ID"

if __name__ == '__main__':
    app.run(debug=True)