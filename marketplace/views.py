from flask import Blueprint, render_template

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
