
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, FileField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[DataRequired('Enter user name')])
    password=PasswordField("Password", validators=[DataRequired('Enter user password')])
    submit = SubmitField("Login")
    remember_me = BooleanField('Remember Me')

 # this is the registration form
class RegisterForm1(FlaskForm):
    user_name=StringField("User Name", validators=[DataRequired()])
    first_name=StringField("First Name", validator=[DataRequired()])
    Last_name=StringField("Last Name", validator=[DataRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[DataRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #next (submit) button
    next = SubmitField("Next")

class RegisterForm2(FlaskForm):
    #avatar=FileField("Upload avatar", validators=[regexp(u'^[^/\\]\.jpg$'), regexp(u'^[^/\\]\.png$'), regexp(u'^[^/\\]\.jpeg$'), 
                #regexp(u'^[^/\\]\.gif$')])
    # I need help with this I can't figure out how to make it work, if seller then allow bio else buyer
    #account_seller=BooleanField()
    #if account_seller = true
    biography=TextAreaField("Bio", validators=[Length(max=1000, message="The length of the bio must be less than 1000 words.")] )
    next = SubmitField("Next")

class RegisterForm3(FlaskForm):
    categories=SelectMultipleField(choices=["Abstract", "Art Deco", "Art Nouveau", "Baroque", "Bahaus", "Classical Realism", "Conceptual"
                "Cubism", "Digital", "Environmental", "Excessivism", "Expressionism", "Fantasy", "Figurative", "Fine Art", "Folk", "Futurism",
                "Geometric", "Graffiti", "Gothic", "Hyperrealism", "Impressionism", "International", "Kitsch", "Land", "Metaphysical", 
                "Minimalism", "Modernism", "Neoism", "Photorealism", "Pixel", "Pop", "Realism", "Romanticism", "Surrealism"])
