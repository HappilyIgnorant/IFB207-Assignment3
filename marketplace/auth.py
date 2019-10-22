from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails
from flask_login import login_user, login_required,logout_user
from . import db
import datetime

#create a blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.user_name.data, form.remember_me.data))
            return redirect('/')
        return render_template('login.html', title='Log In', form=form)
    else:
        email=request.form.get('email_id')
        password=request.form.get('password')
        remember = True if request.form.get('remember_me') else False

        user = User.query.filter_by(email=email).first()
        print(user)
        print(User.query.filter_by(email=email).first())
        if not user and not check_password_hash(user.password_hash, password):
            flash('Please check your login details and try again.')
            print("fail")
            return redirect(url_for('auth.login'))
            

        login_user(user, remember=remember)
        return redirect(url_for('main.item_manage'))


@auth.route('/register' ,methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        form1 = RegisterForm1()     
        form3 = RegisterForm3()
        return render_template("registration.html", title='Sign Up',  f1=form1, f3=form3)
    else:
        email=request.form.get('email_id')
        firstn=request.form.get('first_name')
        lastn=request.form.get('last_name')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        biography=request.form.get('biography')

        user=User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists.')
            return redirect(url_for('auth.register'))



        print(email)
        print(firstn)
        print(lastn)
        print(password)
        print(confirm)
        print(biography)

        new_user = User(email=email, first_name=firstn,last_name=lastn, profile=biography,join_date=datetime.datetime.now(), password_hash=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return render_template("item_manage.html")
        #redirect to somewhere


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
