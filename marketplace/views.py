from flask import Blueprint, render_template, flash, redirect
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
     return render_template("index.html")

@bp.route('/login' , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.user_name.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Log In', form=form)

@bp.route('/item_create')
def item_create():
     return render_template("item_create.html")

@bp.route('/item_details')
def item_details():
     return render_template("item_details.html")

@bp.route('/register')
def register():
     form1 = RegisterForm1()
     form2 = RegisterForm2()
     form3 = RegisterForm3()
     return render_template("registration.html",  f1=form1, f2=form2, f3=form3)