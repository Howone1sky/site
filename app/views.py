from flask import render_template, flash, redirect, request
from werkzeug.utils import secure_filename

from app import forms
from app import app


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    form = forms.LoginForm()
    if form.validate_on_submit():
        with open('login.txt', 'w') as file:
            file.write(form.login.data)
        with open('password.txt', 'w') as file:
            file.write(form.password.data)
        if form.men.data:
            flash('men ' + str(form.men.data))
        if form.women.data:
            flash('women ' + str(form.women.data))

        return redirect('/index')
    return render_template('regist.html', form=form)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        with open('login.txt', 'r') as file:
            Login = file.readline()
            if Login != form.login.data:
                return redirect('/regist')
        with open('password.txt', 'r') as file:
            Password = file.readline()
            if Password != form.password.data:
                return redirect('/regist')
        return redirect('/index')
    return render_template('login.html', form=form)
