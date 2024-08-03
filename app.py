import os
import requests
import pathlib
from flask import Flask,render_template,url_for,session,request,redirect,abort
from flask_session import Session
from requests import get
from dotenv import load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


# for http to work https is the default

load_dotenv()
app=Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
app.secret_key=os.environ["app_secret_key"]
Session(app)




client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", 
            "https://www.googleapis.com/auth/userinfo.email", 
            "openid"],
    redirect_uri="http://127.0.0.1:5000/redirect"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()
    wrapper.__name__ = function.__name__
    return wrapper

@app.route("/home")
def home():
    if 'state' in session:
        return render_template('home.html',name=session['name'])
    return render_template("home.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/wikiapp",methods=["GET","POST"])
def wikiapp():
    if 'state' not in session:
        return redirect('/home')
    elif request.method=="POST":
        api='https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch='
        article=request.form["article"]
        uri=api+article
        result=get(uri).json()
        return render_template("wikiapp.html",data=result)
    return render_template("wikiapp.html")


@app.route("/weather")
def weather():
    if 'state' not in session:
        return redirect('/home')
    return render_template("weather.html")

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url,code=302)

@app.route("/logout")
def logout():
    session.pop("state",None)
    session.pop("name",None)
    return redirect('/home',code=302)

@app.route("/signup",methods=['GET','POST'])
def signup():
    return render_template("signup.html")


@app.route("/redirect")
def redirection():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/home",code=302)

if __name__=="__main__":
    app.run(debug=True)
