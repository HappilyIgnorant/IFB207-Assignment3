from flask import Blueprint, render_template
from .forms import RegisterForm1, RegisterForm2, RegisterForm3

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
     return render_template("index.html")

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
     return render_template("registration.html", 
     form1 = form1, form2 = form2, form3 = form3)
