from app import app
from flask import render_template
# from Admin import Create_accout_cls
from app.data_base import Posts, db, Create_accout_cls
import json

with open('G:\\__Coding__\\___Projects___\\Flask_blog_app\\app\\user.json', 'r') as f:
    params = json.load(f)['params']

@app.route('/')
def index():
    all_posts = Posts.query.filter_by().all() [0:params['number_of_posts_on_home']]
    return render_template('/Public/home.html', posts=all_posts,params=params )

@app.route('/blog')
def blog():
    allpost = Posts.query.filter_by().all() [0:params['number_of_posts_on_blog']]
    return render_template('/Public/blog.html', posts = allpost)

@app.route('/about')
def about():
    return render_template('/Public/about.html')

@app.route('/view/<string:slug>', methods = ['GET'])
def blogView(slug):
    posts = Posts.query.filter_by(slug=slug).first()
    return render_template('/Public/blog-view.html', posts =posts, slug = slug)

