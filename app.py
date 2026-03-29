from flask import Flask,render_template,Blueprint
def create_app():
  app=Flask(__name__)
  from internal.choice import choice
  from logsig.home import homies
  from logsig.login import auth
  from logsig.sign import logsig
  from internal.order import order
  app.register_blueprint(homies)   
  app.register_blueprint(auth)  
  app.register_blueprint(logsig) 
  app.register_blueprint(choice)
  app.register_blueprint(order)
  return app


