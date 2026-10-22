from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

class InterviewReport(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(100))

    overall = db.Column(db.Integer)

    emotion = db.Column(db.String(50))

    eye = db.Column(db.Integer)

    confidence = db.Column(db.Integer)

    date = db.Column(db.String(50))