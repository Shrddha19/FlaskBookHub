from flask import Blueprint,render_template,redirect,url_for,request,flash
order=Blueprint("order",__name__)
@order.route("/order1")
def img1():
    if request.method=="POST":
        name=request.form["name"]
        address=request.form["address"]
        email=request.form["email"]
        if name=="" or email=="" or address=="":
            flash ("plz fill required detail")
        else:
            flash("<h1>Order Placed</h1>")
              
    return render_template("orders/order1.html")




@order.route("/order2")
def img2():
    return render_template("orders/order2.html")

@order.route("/order3")
def img3():
    return render_template("orders/order3.html")

@order.route("/order4")
def img4():
    return render_template("orders/order4.html")