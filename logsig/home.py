from flask import Blueprint,render_template,redirect,url_for,request

homies=Blueprint("homies" ,__name__)
@homies.route("/")
def home():
    return render_template("home.html")
    