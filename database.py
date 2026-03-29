import mysql.connector as mp
def signin():
  conn1=mp.connect(host="localhost", user="root" , database="lab",password="your password")
  return conn1
def logins():
  conn2=mp.connect(host="localhost", user="root" , database="lab",password="your password")
  return conn2
