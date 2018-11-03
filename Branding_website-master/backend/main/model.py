from main import db
from flask_marshmallow import Marshmallow

from main import ma

class User(db.Model):
    __tablename__ = 'User'
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),primary_key=True)
    phone_no = db.Column(db.String(255))

    def __init__(self, password, username, email, phone_no):
        self.password = password
        self.username = username
        self.email = email
        self.phone_no = phone_no

class UserSchema(ma.Schema):
    class Meta:
        fields = ('password', 'username', 'email', 'phone_no')

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class Details(db.Model):
    __tablename__ = 'Details'
    emailid = db.Column(db.String(255), primary_key = True)
    name = db.Column(db.String(255))
    dob = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    referral_code = db.Column(db.String(255))
    in_college = db.Column(db.String(255))
    university_name = db.Column(db.String(255))
    college_name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    category = db.Column(db.String(255))
    instagram = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    tiktok  = db.Column(db.String(255))
    youtube = db.Column(db.String(255))
    blogs = db.Column(db.String(255))

    def __init__(self, emailid, name, dob, gender, referral_code, in_college, university_name, college_name, city, category, instagram, facebook, tiktok, youtube, blogs):
        self.emailid = emailid
        self.name = name
        self.dob = dob
        self.gender = gender
        self.referral_code = referral_code
        self.in_college = in_college
        self.university_name = university_name
        self.college_name = college_name
        self.city = city
        self.category = category
        self.instagram = instagram
        self.facebook = facebook
        self.tiktok  = tiktok
        self.youtube = youtube
        self.blogs = blogs
      
            
class DetailsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('emailid', 'name', 'dob', 'gender', 'referral_code', 'in_college', 'university_name', 'college_name', 'city', 'category', 'instagram', 'facebook', 'tiktok', 'youtube', 'blogs')

details_schema = DetailsSchema()
detailss_schema = DetailsSchema(many=True)

class Campaign(db.Model):
    __tablename__ = 'Campaign'
    campaignid = db.Column(db.String(255), primary_key = True)
    campaign_name = db.Column(db.String(255))
    campaign_startdate = db.Column(db.String(255))
    campaign_venue = db.Column(db.String(255))
    campaign_enddate = db.Column(db.String(255))
    description = db.Column(db.String(255))
    eligibility = db.Column(db.String(255))
    theme = db.Column(db.String(255))
    campaign_picture = db.Column(db.String(255))
    completed = db.Column(db.String(255))


    def __init__(self, campaignid, campaign_name, campaign_startdate, campaign_venue, campaign_enddate, description, eligibility, theme, campaign_picture, completed):
        self.campaignid = campaignid
        self.campaign_name = campaign_name
        self.campaign_startdate = campaign_startdate
        self.campaign_venue = campaign_venue
        self.campaign_enddate = campaign_enddate
        self.description = description
        self.eligibility = eligibility
        self.theme = theme
        self.campaign_picture = campaign_picture  
        self.completed = completed    
            
class CampaignSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('campaignid', 'campaign_name', 'campaign_startdate', 'campaign_venue', 'campaign_enddate', 'description', 'eligibility', 'theme', 'campaign_picture', 'completed')

campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)


class Access_Token(db.Model):
    __tablename__ = 'Access_Token'
    fb_access = db.Column(db.String(255))
    insta_access = db.Column(db.String(255))
    email = db.Column(db.String(255),primary_key=True)

    def __init__(self, fb_access, insta_access, email):
        self.fb_access = fb_access
        self.insta_access = insta_access
        self.email = email

class Access_TokenSchema(ma.Schema):
    class Meta:
        fields = ('fb_access', 'insta_access', 'email')

access_token_schema = Access_TokenSchema()
access_tokens_schema = Access_TokenSchema(many=True)
