from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SWLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class TODO (db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/", methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = TODO(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
    allTODO = TODO.query.all()
    return render_template('index.html',allTODO = allTODO)
    # return "<p>Hello, World!</p>"

@app.route('/show')
def products():
    allTODO = TODO.query.all()
    print(allTODO)
    return "This is my product page"

if __name__ == "__main__":
    app.run(debug=True,port=8000)