from app import app
from flask import render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from app.data_base import Posts, db, Create_accout_cls

app.config['SECRET_KEY'] = 'oh_so_secret'

all_posts = Posts.query.filter_by().all

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
            return redirect(url_for('dishbord', posts = all_posts))
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
                session['user'] = name
                all_posts = Posts.query.filter_by().all()
                return render_template('/Admin/dishbord.html', posts = all_posts, name = name)
            else:
                return redirect(request.url)
    return render_template('/Public/login.html')


@app.route('/dishbord')
def dishbord():
    with open('G:\\__Coding__\\___Projects___\\Blog-site-with-flask\\app\\user.json', 'r') as f:
        userdata = json.load(f)['users']

    if 'user' in session and session['user'] == userdata['name']:
                name = userdata['name']
                all_posts = Posts.query.filter_by().all()
                return render_template('/Admin/dishbord.html', posts = all_posts, name = name)
    if request.method == 'POST':
        logindata = request.form
        name = logindata['name']
        password = logindata['password']
        if name == userdata['name'] and password == userdata['password']:
            # Here i was facing the error becuse of the input of the fomr.
            # Every time i pack the input from the chrom form sugitions and i don't konw why it wan't work.
            # Maybe becuse of the chrome stoing the input with some kind of decoding so there for my input and the json file name was't same 
            # So then i was getting the else return.
            session['user'] = name
            all_posts = Posts.query.filter_by().all()
            return render_template('/Admin/dishbord.html', posts = all_posts, name = name)
        else:
                return render_template('/Public/login.html')
    return render_template('/Public/login.html')


@app.route('/porfile')
def porfile():
    return render_template('/Admin/porfile.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


@app.route('/add_posts', methods = ['GET', 'POST'])
def add_posts():
    if request.method == 'POST':
        post_content = request.form
        title = post_content['title']
        slug = post_content['slug']
        content = post_content['content']
        auther = post_content['auther']
        dt = datetime.utcnow().strftime('%d %b %y')
        if title == '' and slug == '' and content == '' and auther == '':
            return "<script> alert('Hy, Fill all the inputs.') </script>"
        else:
            ready_psot = Posts(slug = slug, title = title, content = content, auther = auther,  dt = dt)
            db.session.add(ready_psot)
            db.session.commit()

    return render_template('/Admin/add_newPosts.html')

