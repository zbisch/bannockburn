from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.debug = True
app.config["MONGODB_SETTINGS"] = {'DB': "pomodb"}
db = MongoEngine(app)


@app.route("/")
def hello():
    return "Helloooooo Wooooorld! "+str(dir(db.connect))

if __name__ == "__main__":
    app.run()
