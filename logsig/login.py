from flask import Blueprint,render_template,redirect,url_for,request
from database import logins
from werkzeug.security import generate_password_hash,check_password_hash

auth=Blueprint("auth" ,__name__)
@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        pwd=request.form["pwd"]
        if name=="" or email=="" or len(pwd)<6:
            return "invalid password<br>Try Again"
        else:
            q="select *from logindet where email=%s"
            conn2=logins()
            cur2=conn2.cursor()
            cur2.execute(q,(email,))
            data=cur2.fetchone()
            
                
            
            if data and check_password_hash(data[2],pwd):
                
                  return redirect(url_for("choice.menu"))
                
            else:
                return"user not found"  
            
            
            
            
            
              
    
    return render_template("login.html")
