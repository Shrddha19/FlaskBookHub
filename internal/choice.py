from flask import Blueprint,request,render_template
choice=Blueprint("choice",__name__)
@choice.route("/choice")
def menu():
    return render_template("choice.html")
  