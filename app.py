from flask import Flask,render_template,url_for,request
from database import Database

app=Flask(__name__)
database=Database()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/project/urishortener/<name>")
def urishort(name):
    name="hi"+str(name)
    return name

@app.route("/project/urishortener",methods=['GET','POST'])
def urishorten():
    if request.method=="POST":
        data=database.InsertUriShortener(request.form["uri"])
        data=database.GetSpecificUri(request.form["uri"])
        return render_template("urishortener.html",newuri=data[0],olduri=request.form["uri"]) 
    return render_template("urishortener.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)