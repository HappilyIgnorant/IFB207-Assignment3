
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, FileField, SelectMultipleField, BooleanField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class ItemDetails(FlaskForm):
    AVAILABLE_CHOICES = [('1'),('2')]
    #selling_options = [("1", "Buy"), ("2", "Auction"), ("3", "Buy/Auction")]
    name = StringField("Title", validators=[DataRequired(), Length(max = 75)])
    category = SelectMultipleField("Categories", choices=[AVAILABLE_CHOICES])
    payment = IntegerField("$ - Value in AUD", validators=[DataRequired()])
    options = RadioField('Label', choices=[('value1','Auction'),('value2','Buy'),('value3', 'Auction/Buy')])
    description = TextAreaField("Description", validators=[DataRequired(), Length(max = 5000)])
    image1 = FileField("Image File")
    image2 = FileField("Image File")
    image3 = FileField("Image File")
    image4 = FileField("Image File")
    image5 = FileField("Image File")
    image6 = FileField("Image File")
    image7 = FileField("Image File")
    image8 = FileField("Image File")
    image9 = FileField("Image File")
    image10 = FileField("Image File")
    image11 = FileField("Image File")
    image12 = FileField("Image File")
    post = SubmitField("Post")