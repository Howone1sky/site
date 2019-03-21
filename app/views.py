from flask import render_template, flash, redirect

from app import forms
from app import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('login ' + form.login.data + 'password ' + form.password.data + ', remember_me = ' + str(form.remember_me.data))
        if form.men.data:
            flash(str(form.men.data))
        if form.women.data:
            flash(str(form.women.data))

        return redirect('/index')
    return render_template('login.html', form=form)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')
