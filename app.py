from flask import Flask,render_template,url_for,request,redirect
from requests import get
from dotenv import load_dotenv

app=Flask(__name__)
load_dotenv()
app.secret_key=

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

if __name__=="__main__":
    app.run(debug=True)
