from datetime import datetime
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy # new

from app.database import scan, read, insert


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import User

@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success"
    }
    # out["body"] = User.query.all()
    users = User.query.all()
    out["body"] = []
    for user in users:                                  #This line returns all users in the user table
        user_dict = {}                                  #Create an empty line list
        user_dict["id"] = user.id                       
        user_dict["first_name"] = user.first_name
        user_dict["last_name"] = user.last_name
        user_dict["hobbies"] = user.hobbies
        user_dict["active"] = user.active
        out["body"].append(user_dict)
    return out

@app.route("/users/<int:pk>")
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success",
    }
    user = User.query.filter_by(id=pk).first()
    out["body"] = {
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "hobbies": user.hobbies,
            "active": user.active
        }
    }
    #out["body"] = {"user": user.__dict__}
    return out


@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    # out["user_id"] = insert(
    #     user_data.get("first_name"),
    #     user_data.get("last_name"),
    #     user_data.get("hobbies")
    # )
    return out, 201

@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    # out["update_user"] = insert(
    #     user_data.get("first_name"),
    #     user_data.get("last_name"),
    #     user_data.get("hobbies")
    # )
    db.session.add(
        User(
            first_name=user_data.first_name("first_name"),
            last_name=user_data.last_name("last_name"),
            hobbies=user_data.hobbies("hobbies")
        )
    )
    db.session.commit()
    return out, 201

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent



