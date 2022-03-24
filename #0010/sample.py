from flask import Flask, request
from datetime import datetime
PORT = 5000
app = Flask(__name__)

@app.route('/')
def index():
    value = 'None'
    query = 'key'

    if request.method == 'GET':
        # リクエストがGETの場合の分岐
        if(query in request.args):
            value = request.args.get(query, '') #keyというパラメータを取得する
    return value

if __name__ == "__main__":
    app.run(port=PORT, debug=True)