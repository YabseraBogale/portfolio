import os
import requests
from flask import Flask,render_template,url_for,request,redirect
from requests import get
from dotenv import load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


load_dotenv()
app=Flask(__name__)

app.secret_key=os.environ["app_secret_key"]


# for http to work https is the default
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@app.route("/wikiapp",methods=["GET","POST"])
def wikiapp():
    if request.method=="POST":
        api='https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch='
        article=request.form["article"]
        uri=api+article
        result=get(uri).json()
        return render_template("wikiapp.html",data=result)
    return render_template("wikiapp.html")


@app.route("/signup",methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/redirect")
def redirect():
    return "redirect"

if __name__=="__main__":
    app.run(debug=True)
