from app import app
from flask import render_template,session

@app.route('/')
def index():
    return render_template('/Public/home.html')

@app.route('/blog')
def blog():
    return render_template('/Public/blog.html')

@app.route('/about')
def about():
    return render_template('/Public/about.html')
@app.route('/vew')
def blogView():
    return render_template('/Public/blog-view.html')

