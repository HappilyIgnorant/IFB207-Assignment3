from flask import Blueprint, render_template, flash, redirect, session, request, url_for
from .forms import RegisterForm1, RegisterForm2, RegisterForm3, LoginForm, ItemDetails, SearchForm, BidForm, SelectForm
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
     session['seller'] = False
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
          if form.validate_on_submit():
               title = request.form.get('name')
               category = request.form.get('category')
               price = request.form.get('price')
               option = request.form.get('options')
               description = request.form.get('description')
               
               addresses = ""
               #Image uploading
               image_forms = ['image1']
               for i in image_forms:
                    try:
                         filename=request.form.get(i)
                         if(filename!=''):
                              f = request.files[i]
                              if f:
                                   filename = secure_filename(f.filename)
                                   f.save(os.path.join(create_app().config['UPLOAD_FOLDER'], filename))
                                   if addresses == "":
                                        addresses = filename
                                   else:
                                        addresses += "," + filename
                    except:
                         continue
          
               new_item = Artwork(seller_id = current_user.id, image_address = addresses, create_date = datetime.datetime.now(), name = title, category = category, price = price, description = description, availability = True)
               db.session.add(new_item)
               db.session.commit()
               return redirect(url_for('main.manage_list'))
          
          return render_template("item_create.html", form = form)
     

@bp.route('/item_details/<id>', methods=['GET', 'POST'])
def item_details(id):
     session['seller'] = False
     bid = BidForm()
     artwork = Artwork.query.filter_by(id = id).first()
     art_images = artwork.image_address.split(",")
     images_count = len(art_images)
     seller = User.query.filter_by(id = artwork.seller_id).first()
     bidded = ''
     if current_user.is_authenticated:
          bidded = Bid.query.filter_by(artwork_id = id, bidder = current_user.id).first()
     sold_date = ''
     if artwork.availability == False:
          sold_date = Purchase.query.filter_by(artwork_id = id).first()
          sold_date = str(sold_date.date).split(' ')[0].split('-')
          sold_date = sold_date[2]+'/'+sold_date[1]+'/'+sold_date[0]
     if request.method=='GET':
          return render_template("item_details.html", form = bid, artwork = artwork, seller = seller, images_count = images_count, art_images = art_images, bidded = bidded, sold_date = sold_date)
     else:
          if bid.validate_on_submit():
               new_bid= Bid(artwork_id = id, bidder = current_user.id, seller = artwork.seller_id, date = datetime.datetime.now())
               db.session.add(new_bid)
               db.session.commit()
               return redirect(url_for('main.item_details', id = id))
          
          return render_template("item_details.html", form = bid, artwork = artwork, seller = seller, images_count = images_count, art_images = art_images, bidded = bidded, sold_date = sold_date)

@bp.route('/buy')
def buy():
     seller=False
     session['seller'] = False
     artwork = Artwork.query.all()
     return render_template("index.html", artwork = artwork)
     

@bp.route('/past_sales')
@login_required
def past_sales():
     session['seller'] = True
     sales = Purchase.query.filter_by(seller = current_user.id)
     num_sales = Purchase.query.filter_by(seller = current_user.id).count()
     sale_info = db.session.query(Purchase, User, Artwork).filter(Purchase.artwork_id == Artwork.id, Purchase.buyer == User.id, Purchase.seller == current_user.id).order_by(db.desc(Purchase.date))
     dates = []
     for sale in sales:
          date = str(sale.date).split(' ')[0].split('-')
          date = date[2]+'/'+date[1]+'/'+date[0]
          dates.append(date)
     return render_template("past_sales.html", sales = sales, num_sales = num_sales, dates = dates, sales_info = sale_info)

@bp.route('/manage_list')
@login_required
def manage_list():
     seller= True
     session['seller'] = True
     artwork = Artwork.query.filter_by(seller_id = current_user.id)
     num_results = Artwork.query.filter_by(seller_id = current_user.id).count()
     return render_template("manage_list.html", artworks = artwork, num_results = num_results)


@bp.route('/item_manage/<art_id>', methods=['GET', 'POST'])
@login_required
def item_manage(art_id): # Query based on current_user.id
     session['seller'] = True
     artwork = Artwork.query.filter_by(id = art_id).first()
     art_date = str(artwork.create_date).split(' ')[0].split('-')
     art_date = art_date[2]+'/'+art_date[1]+'/'+art_date[0]
     num_bids = Bid.query.filter_by(artwork_id = art_id).count()
     num_bidders = Bid.query.filter_by(artwork_id = art_id).distinct(Bid.bidder).group_by(Bid.bidder, Bid.id).count()
     bids = Bid.query.filter_by(artwork_id = art_id).order_by(db.desc(Bid.date))
     formatted_dates = []
     formatted_times = []
     bid_counter = 0
     purchase_check = Purchase.query.filter_by(artwork_id = art_id).count()

     form = SelectForm()
     
     for bid in bids:
          date = str(bid.date).split(' ')[0].split('-')
          date = date[2]+'/'+date[1]+'/'+date[0]
          formatted_dates.append(date)
          time = str(bid.date).split(' ')[1].split('.')[0]
          formatted_times.append(time)
          bid_counter += 1
     deposit = round(artwork.price*0.1)
     table_info = db.session.query(Bid, User).filter(Bid.bidder == User.id, Bid.artwork_id == art_id).order_by(db.desc(Bid.date))

     if request.method=='GET':
          return render_template("item_manage.html", artwork = artwork, num_bidders = num_bidders, dates = formatted_dates, times = formatted_times,  deposit = deposit, bids = bids, num_bids = bid_counter, table_info = table_info, art_date = art_date, form = form, check = purchase_check)
     else:
          # for i in range(bid_counter): 
          if form.validate_on_submit():
               buyer_id = request.form.get("buyer_id")
               print(buyer_id)
               new_purchase= Purchase(artwork_id = art_id, buyer = buyer_id, seller = artwork.seller_id, date = datetime.datetime.now(), price = artwork.price, notes = "None")
               artwork.availability = 0 #this should do it
               db.session.add(new_purchase)
               db.session.commit()
               return redirect(url_for('main.past_sales'))
          return render_template("item_manage.html", artwork = artwork, num_bidders = num_bidders, dates = formatted_dates, times = formatted_times,  deposit = deposit, bids = bids, num_bids = bid_counter, table_info = table_info, art_date = art_date, form = form, check = purchase_check)


 #Menu links
 # These are routes for the menu Links  

@bp.route('/artists')
def artists():
     return render_template("_artists.html")

@bp.route('/auctions')
def auctions():
     return render_template("_auctions.html")

@bp.route('/bidded_items')
@login_required
def bidded_items():
     session['seller'] = False
     bids = Bid.query.filter_by(bidder = current_user.id)
     num_results = Bid.query.filter_by(bidder = current_user.id).count()
     artwork = []
     for i in range(num_results):
          artwork.append(Artwork.query.filter_by(id = bids[i].artwork_id).first())
     return render_template("bidded_items.html", bids = bids, num_results = num_results, artworks = artwork)

@bp.route('/oilpainting')
def oilpainting():
     session['seller'] = False
     artworks = Artwork.query.filter_by(category = 'Oil Painting')
     num_results = Artwork.query.filter_by(category = 'Oil Painting').count()
     return render_template("_oil_painting.html", artworks = artworks, num_results = num_results)

@bp.route('/prints')
def prints():
     session['seller'] = False
     artworks = Artwork.query.filter_by(category = 'Print')
     num_results = Artwork.query.filter_by(category = 'Print').count()
     return render_template("_print.html", artworks = artworks, num_results = num_results)

@bp.route('/sculpture')
def sculpture():
     session['seller'] = False
     artworks = Artwork.query.filter_by(category = 'Sculpture')
     num_results = Artwork.query.filter_by(category = 'Sculpture').count()
     return render_template("_sculpture.html", artworks = artworks, num_results = num_results)

@bp.route('/watercolour')
def watercolour():
     session['seller'] = False
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
     users = User.query.all()
     searchTerm=request.form.get("search_string")     
     Art=Artwork.query.filter(Artwork.description.like('%'+searchTerm+'%'))
     Art=Artwork.query.filter(User.seller('%'+searchTerm+'%'))
     #Link name to seller ID, how do I do that...
     print(searchTerm)
     print( Art.count())
     return render_template("results.html", artworks = Art, num_results = Art.count())


# Just to test the page
@bp.route('/404')     
def page_404(error):
     
     return render_template("404.html"), 404

@bp.route('/403')     
def page_403(error):
     return render_template("403.html"), 403

@bp.route('/500')     
def page_500(error):
     return render_template("500.html"), 500
    
@bp.route('/410')     
def page_410(error):
     return render_template("410.html"), 410
     
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