from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    cart = db.relationship('CartItem', backref='user', lazy=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name =db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                                   