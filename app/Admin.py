from app import app
from flask import render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import json

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-blog-site'
app.config['SECRET_KEY'] = 'oh_so_secret'
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
    titel = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(100), nullable = False)

@app.route('/create-acount', methods = ['GET', 'POST'])
def acrate_acount():
    if request.method == "POST":
        data = request.form
        name = data['name']
        last_name = data['last-name']
        email = data['email']
        password = data['password']
        if name == '' and email == '' and password == '':
            return "<script> alert('Hy, Enter some infomations.') </script>"
        else:
            fulldata = Create_accout_cls(name = name, last_name = last_name, email = email, password = password )                
            db.session.add(fulldata)
            db.session.commit()
            return redirect(url_for('dishbord'))
    return render_template('/Admin/create-acount.html')

@app.route('/login', methods = ['POST', 'GET'])
def loginpage():
    if request.method == 'POST':
        logindata = request.form
        name = logindata['name']
        password = logindata['password']
        with open('G:\\__Coding__\\___Projects___\\Blog-site-with-flask\\app\\user.json', 'r') as f:
            userdata = json.load(f)['users']
            if name == userdata['name'] and password == userdata['password']:
                # Here i was facing the error becuse of the input of the fomr.
                # Every time i pack the input from the chrom form sugitions and i don't konw why it wan't work.
                # Maybe becuse of the chrome stoing the input with some kind of decoding so there for my input and the json file name was't same 
                # So then i was getting the else return.
                return render_template('/Admin/dishbord.html')
            else:
                return redirect(request.url)
    return render_template('/Public/login.html')

@app.route('/dishbord')
def dishbord():
    if request.method == 'POST':
        logindata = request.form
        name = logindata['name']
        password = logindata['password']
        with open('G:\\__Coding__\\___Projects___\\Blog-site-with-flask\\app\\user.json', 'r') as f:
            userdata = json.load(f)['users']
            if name == userdata['name'] and password == userdata['password']:
                # Here i was facing the error becuse of the input of the fomr.
                # Every time i pack the input from the chrom form sugitions and i don't konw why it wan't work.
                # Maybe becuse of the chrome stoing the input with some kind of decoding so there for my input and the json file name was't same 
                # So then i was getting the else return.
                return render_template('/Admin/dishbord.html')
            else:
                 return render_template('/Public/login.html')
    return render_template('/Public/login.html')

@app.route('/posts')
def posts():
    return render_template('/Admin/posts.html')

@app.route('/porfile')
def porfile():
    return render_template('/Admin/porfile.html')

@app.route('/logout')
def logout():
    return render_template('/Admin/logout.html')

