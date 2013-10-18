from flask import Flask
from flask import url_for, render_template
#from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.debug = True
#app.config["MONGODB_SETTINGS"] = {'DB': "pomodb"}
#db = MongoEngine(app)


@app.route("/")
def serve_homepage():
    contents = open("static/index.html", "r").read()
    #return render_template(url_for("static", filename="index.html"))
    return contents


def hello():
    return "Helloooooo Wooooorld! "#+str(dir(db))

#class Pomodoro(db.DynamicDocument):
#    name = db.StringField(verbose_name="Name", required=True)

d = {"name" : "Teasdfasdf",
     "username" : "12345"}

#p = Pomodoro(**d)
#p.save()

#c = Comment(note="asdf", body="Adsfasdf", author="asdfwf3f34")


#db('pomos').save("{1:1}")
#c.save()

#class Pomodoro(db.Document):
#    pass
#a = db.Document(note="Asdf")
#a.save()


if __name__ == "__main__":
    app.run()
