from app import db, login 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<Id={self.id} User={self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)        
    

class Proverbs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proverb = db.Column(db.String(300), unique=True, nullable=False)
    translation = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<id={self.id} proverb={self.proverb} translate={self.translation}>'