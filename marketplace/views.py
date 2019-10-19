from flask import Blueprint, render_template, flash, redirect
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Artwork, Bid, Purchase

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

@bp.route('/register' ,methods=['GET', 'POST'])
def register():
     form1 = RegisterForm1()
     
     form3 = RegisterForm3()
     return render_template("registration.html", title='Sign Up',  f1=form1, f3=form3)

@bp.route('/item_create')
def item_create():
     form = form
     return render_template("item_create.html", form = form)
     
@bp.route('/item_details')
def item_details():
     return render_template("item_details.html")



     # if form.validate_on_submit():
     #      # Retrieve the information from form
     #      user_name = form1.user_name.data
     #      first_name = form1.first_name.data
     #      last_name = form1.last_name.data
     #      email = form1.email.data
     #      password_hash = generate_password_hash(form1.password.data)
          

     #      # Store the information to the database
     #      new_user = User() ###### need to add sth



