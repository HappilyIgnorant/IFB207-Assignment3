#import flask - from the package import class
from flask import Flask 
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
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketplace.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['sqlite:///marketplace.sqlite']
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
    
    return app



