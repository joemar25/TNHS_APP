# all necessary imports
from flask import Flask, render_template
    
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    # return a url from templates
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='localhost', port=8080)