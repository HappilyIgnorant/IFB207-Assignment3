
from flask_wtf import FlaskForm
from wtforms import Form, SelectField
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, FileField, SelectMultipleField, BooleanField, RadioField, IntegerField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from flask_wtf.file import FileRequired, FileAllowed


#creates the login information
class LoginForm(FlaskForm):
    email_id = StringField("Email Address", validators=[InputRequired(message="Please enter a valid email."),Email("Please enter a valid email.")])
    password=PasswordField("Password", validators=[InputRequired('Enter password.')])
    submit = SubmitField("Login")
    remember_me = BooleanField('Remember Me')

 # this is the registration form
class RegisterForm1(FlaskForm):
    first_name=StringField("First Name", validators=[DataRequired(message="Please enter your first name")])
    last_name=StringField("Last Name", validators=[DataRequired(message="Please enter your last name")])
    email_id = StringField("Email Address", validators=[DataRequired(message="Please enter a valid email."), Email("Please enter a valid email.")])
    phone_number=IntegerField("Contact Number", validators=[DataRequired(message = "Please enter a valid phone number.")])
    # if you can do that I will leave you to it ---------- I fixed it
    #linking two fields - password should be equal to data entered in confirm
    password= PasswordField("Password", validators=[DataRequired(message='Please enter your password')])
                  
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message="Password must match!")])
       
    #avatar=FileField("Upload avatar", validators=[regexp(u'^[^/\\]\.jpg$'), regexp(u'^[^/\\]\.png$'), regexp(u'^[^/\\]\.jpeg$'), 
                #regexp(u'^[^/\\]\.gif$')])
    # I need help with this I can't figure out how to make it work, if seller then allow bio else buyer
    #account_seller=BooleanField()
    #if account_seller = true
    biography=TextAreaField("About you", validators=[Length(max=1000, message="The length of the bio must be less than 1000 words.")])
    
    #next (submit) button
    next = SubmitField("Next")

class RegisterForm2(FlaskForm):
    next = SubmitField("Next")

class RegisterForm3(FlaskForm):
    AVAILABLE_CHOICES = [('1','1'),('2','2')]
    assigned = SelectMultipleField('Assigned', choices=[AVAILABLE_CHOICES])
    #categories=SelectMultipleField(u'Test me', choices=[("Abstract"), ("Art Deco")])
    #, ("Art Nouveau"), ("Baroque"), ("Bahaus"), ("Classical Realism"), ("Conceptual")])


#                "Cubism", "Digital", "Environmental", "Excessivism", "Expressionism", "Fantasy", "Figurative", "Fine Art", "Folk", "Futurism",
 #               "Geometric", "Graffiti", "Gothic", "Hyperrealism", "Impressionism", "International", "Kitsch", "Land", "Metaphysical", 
  #              "Minimalism", "Modernism", "Neoism", "Photorealism", "Pixel", ("Pop"), ("Realism"), ("Romanticism"), ("Surrealism")])

CATEGORY_CHOICES = [('Oil Painting','Oil Painting'), ('Print','Print'), ('Sculpture', 'Sculpture'), ('Watercolor', 'Watercolor')]
class ItemDetails(FlaskForm):
    
    #selling_options = [("1", "Buy"), ("2", "Auction"), ("3", "Buy/Auction")]
    name = StringField("", validators=[InputRequired(), Length(max = 75)])
    category = SelectField("Categories", choices=CATEGORY_CHOICES)
    price = IntegerField("$ - Value in AUD", validators=[InputRequired(message="Please enter an appropriate price number.")])
    options = RadioField('Label', choices=[('Auction','Auction'),('Buy','Buy'),('Auction/Buy', 'Auction/Buy')], default='Auction')
    description = TextAreaField("Description", validators=[InputRequired(), Length(max = 5000)])
    image1 = FileField("Image File", validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    image2 = FileField("Image File", validators=[FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    image3 = FileField("Image File", validators=[FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    image4 = FileField("Image File", validators=[FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    image5 = FileField("Image File", validators=[FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    image6 = FileField("Image File", validators=[FileAllowed(['png', 'jpg', 'jpeg'], "Please enter an appropriate image file format (Supported: JPG, PNG and JPEG)")])
    post = SubmitField("Post")

class SearchForm(FlaskForm):
    search = StringField('search')

class BidForm(FlaskForm):
    bidButton = SubmitField("Bid")

class SelectForm(FlaskForm):
    selectButton = SubmitField("Confirm")
    test = StringField()