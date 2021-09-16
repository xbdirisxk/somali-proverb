from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, SomaliProverb, UpdateForm
from sqlalchemy import or_
from app.models import User, Proverbs
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SomaliProverb()
    return render_template('index.html', form=form, proverbs=Proverbs.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/create', methods=['GET', 'POST'])
def add():
    form = SomaliProverb()
    if form.validate_on_submit():
        proverb = Proverbs(proverb=form.proverb.data, translation=form.translation.data)
        db.session.add(proverb)
        db.session.commit()
        flash('New proverb added')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    proverb = Proverbs.query.get_or_404(id)
    db.session.delete(proverb)
    db.session.commit()
    flash('proverb deleted')
    return redirect(url_for('index'))

'''@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UpdateForm()
    proverb = Proverbs.query.get_or_404(id)
    if form.save.data:
        proverb.proverb = form.proverb.data
        proverb.translation = form.translation.data
        db.session.commit()
        flash('proverb updated')
        return redirect(url_for('index'))
    return render_template('update.html', form=form)'''

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html", user =current_user.username)