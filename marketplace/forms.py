
from flask_wtf import FlaskForm
from wtforms import Form, SelectField
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, FileField, SelectMultipleField, BooleanField, RadioField, IntegerField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


#creates the login information
class LoginForm(FlaskForm):
    email_id = StringField("Email Address", validators=[DataRequired(), Email("Please enter a valid email")])
    password=PasswordField("Password", validators=[DataRequired('Enter password')])
    submit = SubmitField("Login")
    remember_me = BooleanField('Remember Me')

 # this is the registration form
class RegisterForm1(FlaskForm):
    user_name=StringField("User Name", validators=[DataRequired()])
    first_name=StringField("First Name", validators=[DataRequired()])
    last_name=StringField("Last Name", validators=[DataRequired()])
    email_id = StringField("Email Address", validators=[DataRequired(), Email("Please enter a valid email")])
    phone_number=IntegerField("Contact Number", validators=[DataRequired()])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[DataRequired(message=(u'That\'s not a valid email address.')),])
                  
    confirm = PasswordField("Confirm Password", validators=[ EqualTo(password, message="test")])
       
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
    name = StringField("", validators=[DataRequired(), Length(max = 75)])
    category = SelectField("Categories", choices=CATEGORY_CHOICES)
    price = IntegerField("$ - Value in AUD", validators=[DataRequired(message="Please enter an appropriate price number.")])
    options = RadioField('Label', choices=[('Auction','Auction'),('Buy','Buy'),('Auction/Buy', 'Auction/Buy')], default='Auction')
    description = TextAreaField("Description", validators=[DataRequired(), Length(max = 5000)])
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