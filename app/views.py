from flask import render_template, flash, redirect, request
from werkzeug.utils import secure_filename

from app import forms
from app import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('login ' + form.login.data + ',  password ' + form.password.data + ', remember_me = ' + str(form.remember_me.data))
        if form.men.data:
            flash('men ' + str(form.men.data))
        if form.women.data:
            flash('women ' + str(form.women.data))

        return redirect('/index')
    return render_template('login.html', form=form)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('D:/maxim/tmp/' + secure_filename(f.filename))
        flash('file uploaded')
        return redirect('/index')
    return render_template('upload.html')


@app.route('/test')
def test():
    return render_template('test.html')

