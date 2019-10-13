
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, FileField, SelectMultipleField
from wtforms.validators import InputRequired, Length, Email, EqualTo



#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm1(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #next (submit) button
    next = SubmitField("Next")

class RegisterForm2(FlaskForm):
    #avatar=FileField("Upload avatar", validators=[regexp(u'^[^/\\]\.jpg$'), regexp(u'^[^/\\]\.png$'), regexp(u'^[^/\\]\.jpeg$'), 
                #regexp(u'^[^/\\]\.gif$')])
    biography=TextAreaField("Bio", validators=[Length(max=1000, message="The length of the bio must be less than 1000 words.")] )
    next = SubmitField("Next")

class RegisterForm3(FlaskForm):
    categories=SelectMultipleField(choices=["Abstract", "Art Deco", "Art Nouveau", "Baroque", "Bahaus", "Classical Realism", "Conceptual"
                "Cubism", "Digital", "Environmental", "Excessivism", "Expressionism", "Fantasy", "Figurative", "Fine Art", "Folk", "Futurism",
                "Geometric", "Graffiti", "Gothic", "Hyperrealism", "Impressionism", "International", "Kitsch", "Land", "Metaphysical", 
                "Minimalism", "Modernism", "Neoism", "Photorealism", "Pixel", "Pop", "Realism", "Romanticism", "Surrealism"])
