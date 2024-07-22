from flask import Flask,render_template,url_for,request,redirect
from database import Database
# # wtf is wrong with github deleteing doesn't count
app=Flask(__name__)
database=Database()

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/weather")
def weather():
    return render_template("weather.html")

if __name__=="__main__":
    app.run(debug=True)
