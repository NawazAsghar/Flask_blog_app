from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-blog-site'

db = SQLAlchemy(app)

class Create_accout_cls(db.Model):
    __tablename__ = 'create-accounts'
    serial_no = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable = False)
    last_name = db.Column(db.String(15), nullable = True)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(100), nullable = False)

class Posts(db.Model):
    __tablename__ = 'posts'
    post_sno = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(15), nullable = False)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(1000), nullable = False)
    auther = db.Column(db.String(15), nullable = False)
    dt = db.Column(db.String(10), nullable = False)