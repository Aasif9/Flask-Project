from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    college = db.Column(db.String(80))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        roll = request.form['roll']

        student = Student(name=name, college=college, roll=roll)
        db.session.add(student)
        db.session.commit()

    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/submit', methods=['GET', 'POST'])
def submits():
    name = request.form.get("name")
    college = request.form.get("college")
    roll = request.form.get("roll")
    #    return "Name : " + name + "College: " + college + "Roll No : " + roll
    return render_template("submission.html", name=name, college=college, roll=roll)





if __name__ == '__main__':
    db.create_all()
    app.run()
