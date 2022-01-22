from flask import Flask, request, jsonify
import time

app = Flask(__name__)
@app.route("/bot",method=['POST'])


# response
def response():
    query = dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)