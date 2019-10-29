#import flask - from the package import class
from flask import Flask ,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
global seller
from .models import User, Artwork, Bid, Purchase

# create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    #set the app configuration data 
    #use heroku postgresql both locally and remotely
    # app.config['SQLALCHEMY_DATABASE_URI']='postgres://dmkcxxmnrnzqmv:12b2d1f6075ae5232d1dfd1b2d4222cca4414a773030f622cc98044c0b1f66af@ec2-174-129-253-101.compute-1.amazonaws.com:5432/d5lrdgfpnqvdun'
    #app.config['SQLALCHEMY_DATABASE_URI']=os.environ['sqlite:///marketplace.sqlite']
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketplace.sqlite'
    dirname = os.path.dirname(__file__)
    app.config['UPLOAD_FOLDER'] = os.path.join(dirname, 'static/img/')

    app.debug=True
    app.secret_key='utroutoru'
    
    #initialize db with flask app
    db.init_app(app)

    seller=False

    bootstrap = Bootstrap(app)
    
    #initialize the login manager
    login_manager = LoginManager()
    
    #set the name of the login function that lets user login
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    #from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    #importing views module here to avoid circular references
    # a commonly used practice.
    from . import views
    app.register_blueprint(views.bp)

    from . import auth
    app.register_blueprint(auth.auth)

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("403.html"),403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"),404
    
    @app.errorhandler(410)
    def page_deleted(e):
        return render_template("410.html"),410 

    @app.errorhandler(500)
    def internal_error(e):
        return render_template("500.html"),500 

    return app



