from flask import Flask,render_template,url_for,redirect
from requests import get
from flask_cors import CORS
app=Flask(__name__)
CORS(app,origins=["http://127.0.0.1:5000/wikiapp"])

@app.route("/wikiapp",methods=["GET","POST"])
def wikiapp():
    if request.method=="POST":
        api='https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch='
        article=request.form["article"]
        uri=api+article
        return get(uri)
    return render_template("wikiapp.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

if __name__=="__main__":
    app.run(debug=True)
