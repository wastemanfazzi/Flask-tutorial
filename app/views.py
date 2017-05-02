from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    if not 'user' in session:
        return redirect('/login')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))

        session['user'] = form.openid.data

        return redirect('/index')

    return render_template('login.html',
                            title= 'Sign in',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    # session.pop('user')
    session.clear()
    return redirect('/')
