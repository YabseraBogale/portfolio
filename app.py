import os
import requests
import pathlib
from flask import Flask,render_template,url_for,request,redirect
from requests import get
from dotenv import load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


load_dotenv()
app=Flask(__name__)
# for http to work https is the default
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
app.secret_key=os.environ["app_secret_key"]
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/redirect"
)
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
