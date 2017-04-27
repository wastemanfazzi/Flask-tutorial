from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Fazzi'}
    posts = [
        {
            'author': {'nickname':'Zen Shaw'},
            'body': 'Beautiful day for a Meat Module!'
        },
        {
            'author': {'nickname':'Alberto'},
            'body': 'Everything in the world is because Portugal exists'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
