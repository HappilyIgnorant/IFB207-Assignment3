from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # Login Credentials
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Basic information
    name = db.Column(db.String(100), nullable = False)
    profile = db.Column(db.String(10000), default = "N/A")
    favourites = db.Column(db.String(1000), default = "N/A")
    join_date = db.Column(db.DateTime, nullable = False)
    is_seller = db.Column(db.Boolean, default = False)

    # Relation to other tables
    artworks = db.relationship('Artwork', backref = 'user')
    bids = db.relationship('Bid', backref = 'user')
    purchases = db.relationship('Purchase', backref = 'user')
    
class Artwork(db.Model):
    __tablename__ = 'artworks'
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_address = db.Column(db.String(500), nullable = False)
    create_date = db.Column(db.DateTime, nullable = False)

    name = db.Column(db.String(1000), nullable = False)
    category = db.Column(db.String(300), nullable = False)
    description = db.Column(db.String(1000), nullable = False)
    price = db.Column(db.Float(precision=2), nullable = False)
    availability = db.Column(db.Boolean, default = True)

    # Relation to other tables
    bids = db.relationship('Bid', backref = 'artwork')
    purchase = db.relationship('Purchase', backref = 'artwork')

class Bid(db.Model):
    __tablename__ = "bids"
    id = db.Column(db.Integer, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    bidder = db.Column(db.Integer, db.ForeignKey('users.id'))
    seller = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, nullable = False)

class Purchase(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    buyer = db.Column(db.Integer, db.ForeignKey('users.id'))
    seller = db.Column(db.Integer, db.ForeignKey('users.id'))

    date = db.Column(db.DateTime, nullable = False)
    price = db.Column(db.Float(precision=2), nullable = False)

    notes = db.Column(db.String(500))
