from flask import Blueprint, render_template, flash, redirect, session, request
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug import secure_filename
from . import db
from .models import User, Artwork, Bid, Purchase
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
import os


#import flask_whooshalchemy

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
     return render_template("index.html")

@bp.route('/item_create', methods=['GET', 'POST'])
# @login_required
def item_create():
     if request.method=='GET':
          form = ItemDetails()
          return render_template("item_create.html", form = form)
     else:
          form = ItemDetails()

          title = request.form.get('name')
          category = request.form.get('category')
          price = request.form.get('price')
          option = request.form.get('options')
          description = request.form.get('description')
          print(title, category, price, option, description)

          # #image uploading
          # image1 = secure_filename(form.image1.filename)
          # print(image1)
          
          
          return render_template("item_create.html", form = form)
     
     
@bp.route('/item_details')
def item_details():
     return render_template("item_details.html")

@bp.route('/sell')
def sell():
     seller=True
     session['seller'] = True
     return render_template("item_manage.html")

@bp.route('/buy')
def buy():
     seller=False
     session['seller'] = False
     return render_template("index.html")
     
@bp.route('/item_manage')
@login_required
def item_manage():

     return render_template("item_manage.html")


 #Menu links
 # These are routes for the menu Links  

@bp.route('/artists')
def artists():
     return render_template("_artists.html")

@bp.route('/auctions')
def auctions():
     return render_template("_auctions.html")

@bp.route('/fineart')
def fineart():
     return render_template("_fineart.html")

@bp.route('/modernart')
def modernart():
     return render_template("_modernart.html")
@bp.route('/sculpture')
def sculpture():
     return render_template("_sculpture.html")
@bp.route('/abstract')
def abstract():
     return render_template("_abstract.html")
@bp.route('/commission')
def commission():
     return render_template("_commision.html")

@bp.route('/gallery')
def gallery():
     return render_template("_gallery.html")

@bp.route('/results')
def search_results(search):
     artworks = Artwork.query.woosh_search(request.args.get('query')).all
     num_results = Artwork.query.filter_by(category = 'Realism').count()
     return render_template("results.html", artworks = artworks, num_results = num_results)
     
     #artworks = Artwork.query.filter_by(category = 'Realism')
     #num_results = Artwork.query.filter_by(category = 'Realism').count()
     #return render_template("results.html", artworks = artworks, num_results = num_results)
