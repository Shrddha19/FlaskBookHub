from flask import Blueprint,redirect,url_for,render_template,request,flash
from database import signin
from werkzeug.security import generate_password_hash
logsig=Blueprint("authe",__name__)
@logsig.route("/sign",methods=["GET","POST"])
def signi():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        pwd=request.form["pwd"]
        if name=="" or email=="" or len(pwd)<6:
            return "invalid password<br>Try Again"
        else:
            q="insert into logindet values(%s,%s,%s )"
            s=generate_password_hash(pwd)
            sel=(name,email,s)
            conn1=signin()
            cur1=conn1.cursor()
            cur1.execute(q,sel)
            conn1.commit()
            return redirect(url_for("choice.menu"))
    
    
    return render_template("sign.html")