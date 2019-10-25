from flask import Blueprint, render_template, flash, redirect, session, request
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails, SearchForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from . import db
from .models import User, Artwork, Bid, Purchase
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
import os
from . import create_app
import datetime


#import flask_whooshalchemy

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
     artwork = Artwork.query.all()
     return render_template("index.html", artwork = artwork)



@bp.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
     seller=True
     session['seller'] = True
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
          
          addresses = ""
          #Image uploading
          image_forms = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10']
          for i in image_forms:
               f = request.files[i]
               if f:
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(create_app().config['UPLOAD_FOLDER'], filename))
                    if addresses == "":
                         addresses = filename
                    else:
                         addresses += "," + filename
     
          new_item = Artwork(seller_id = current_user.id, image_address = addresses, create_date = datetime.datetime.now(), name = title, category = category, price = price, description = description, availability = True)
          db.session.add(new_item)
          db.session.commit()
          
          return render_template("item_create.html", form = form)
     
     
@bp.route('/item_details/<id>')
def item_details(id):
     artwork = Artwork.query.filter_by(id = id).first()
     seller = User.query.filter_by(id = artwork.seller_id).first()
     return render_template("item_details.html", artwork = artwork, seller = seller)

@bp.route('/buy')
def buy():
     seller=False
     session['seller'] = False
     artwork = Artwork.query.all()
     return render_template("index.html", artwork = artwork)
     

@bp.route('/select-item')
@login_required
def select_item():
     artworks = Artwork.query.all()
     return render_template("item_manage.html")

@bp.route('/item_manage')
@login_required
def item_manage(): # Query based on current_user.id
     artworks = Artwork.query.all() #_
     return render_template("item_manage.html")


 #Menu links
 # These are routes for the menu Links  

@bp.route('/artists')
def artists():
     return render_template("_artists.html")

@bp.route('/auctions')
def auctions():
     return render_template("_auctions.html")

@bp.route('/oilpainting')
def oilpainting():
     artworks = Artwork.query.filter_by(category = 'Oil Painting')
     num_results = Artwork.query.filter_by(category = 'Oil Painting').count()
     return render_template("_oil_painting.html", artworks = artworks, num_results = num_results)

@bp.route('/prints')
def prints():
     artworks = Artwork.query.filter_by(category = 'print')
     num_results = Artwork.query.filter_by(category = 'print').count()
     return render_template("_print.html", artworks = artworks, num_results = num_results)

@bp.route('/sculpture')
def sculpture():
     artworks = Artwork.query.filter_by(category = 'Sculpture')
     num_results = Artwork.query.filter_by(category = 'Sculpture').count()
     return render_template("_sculpture.html", artworks = artworks, num_results = num_results)

@bp.route('/watercolour')
def watercolour():
     artworks = Artwork.query.filter_by(category = 'Watercolor')
     num_results = Artwork.query.filter_by(category = 'Watercolor').count()
     return render_template("_watercolour.html", artworks = artworks, num_results = num_results)


@bp.route('/gallery')
def gallery():
     artworks = Artwork.query.all()
     num_results = Artwork.query.count()
     return render_template("_gallery.html", artworks = artworks, num_results = num_results)

@bp.route('/results', methods=['POST'])
def search_results():
     searchTerm=request.form.get("search_string")     
     Art=Artwork.query.filter(Artwork.description.like('%'+searchTerm+'%'))
     print(searchTerm)
     print( Art.count())
     return render_template("results.html", artworks = Art, num_results = Art.count())

     

     
     #return render_template("results.html")

     # else: #Okay, just revert back when you want to test
     # Okay can do but at the moment I'm still scratchign my head lol, so I feel like I should just copy the registration form a little
     # yeah you can ahha

     
     #artworks = Artwork.query.woosh_search(request.args.get('query')).all
     #num_results = Artwork.query.filter_by(category = 'Realism').count()
     #return render_template("results.html", artworks = artworks, num_results = num_results)
     
     #artworks = Artwork.query.filter_by(category = 'Realism')
     #num_results = Artwork.query.filter_by(category = 'Realism').count()
     #return render_template("results.html", artworks = artworks, num_results = num_results)