#!/usr/bin/python
from users import User
from flask import Flask, render_template, redirect, url_for, request
from database import db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    return "hello World!"

@app.route("/user", methods=["GET", "POST"])
def user_page():
    systemusers = []
    if request.method == "POST":
        new_user_firstName = request.form.get("firstName", "")
        new_user_lastName = request.form.get("lastName", "")
        new_user_emailAddress = request.form.get("emailAddress", "")

        new_user = User(new_user_firstName,new_user_lastName,new_user_emailAddress)

        user = db.posts

        user_data = {
            'firstName': new_user_firstName,
            'lastName': new_user_lastName,
            'emailAddress': new_user_emailAddress
        }
        result = user.insert_one(user_data)
        print('One User: {0}'.format(result.inserted_id))

        systemusers = "user.find({})"

        return redirect(url_for("user_page"))
    return render_template("index.html", users=systemusers)



if __name__ == "__main__":
    app.run(debug=True)



