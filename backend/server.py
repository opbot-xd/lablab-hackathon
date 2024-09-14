from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World!"
@app.route("/get_data")
def getdata():
    return "Your data"


if __name__ == "__main__":
    app.run()