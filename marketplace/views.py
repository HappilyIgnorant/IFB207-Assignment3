from flask import Blueprint, render_template, flash, redirect
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Artwork, Bid, Purchase
from flask_login import login_required

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
     return render_template("index.html")


@bp.route('/item_create')
def item_create():
     form = form
     return render_template("item_create.html", form = form)
     
@bp.route('/item_details')
def item_details():
     return render_template("item_details.html")

@bp.route('/item_manage')
@login_required
def item_manage():

     return render_template("item_manage.html")



     # if form.validate_on_submit():
     #      # Retrieve the information from form
     #      user_name = form1.user_name.data
     #      first_name = form1.first_name.data
     #      last_name = form1.last_name.data
     #      email = form1.email.data
     #      password_hash = generate_password_hash(form1.password.data)
          

     #      # Store the information to the database
     #      new_user = User() ###### need to add sth



