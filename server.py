from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojosurvey.html")   

@app.route('/result', methods =['POST'])
def result_info():
    print ("Data Received")
    username = request.form['username']
    dojolocation = request.form['dojolocation']
    favlanguage = request.form['favlanguage']
    commentarea = request.form['commentarea']
    print (username, dojolocation, favlanguage, commentarea)
    return render_template("result.html", username=request.form['username'], dojolocation=request.form['dojolocation'], favlanguage = request.form['favlanguage'], commentarea = request.form['commentarea'])

if __name__ == "__main__":
    app.run(debug = True)