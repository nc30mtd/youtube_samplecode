from flask import Flask, request, render_template
from datetime import datetime
PORT = 5000
app = Flask(__name__)

@app.route('/')  #追加
def index():
    return render_template("index.html")

@app.route('/sample', methods=["POST"])  #追加
def sample():
    value = 'None'
    if request.method == 'POST': # リクエストがPOSTの場合の分岐
        if("username" in request.form): # パラメータ内にquery(ここでは'key')があれば分岐
            value = request.form["username"] +'さんこんにちは'
    return value

if __name__ == "__main__":
    app.run(port=PORT, debug=True)