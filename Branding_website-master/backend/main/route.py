from flask import request, jsonify
from main import app
from main.model import User, user_schema, users_schema, UserSchema, details_schema, detailss_schema, Details, DetailsSchema, Campaign, CampaignSchema, campaign_schema, campaigns_schema
from flask_marshmallow import Marshmallow
from main import db



@app.route("/register_user", methods=["POST"])
def register_user():
    emailid = request.form['emailid']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    referral_code = request.form['referral_code']
    in_college = request.form['in_college']
    university_name = request.form['university_name']
    college_name = request.form['college_name']
    city = request.form['city']
    category = request.form['category']
    instagram = request.form['instagram']
    facebook = request.form['facebook']
    tiktok  = request.form['tiktok']
    youtube = request.form['youtube']
    blogs = request.form['blogs']

    
    
    new_registration = Details(emailid, name, dob, gender, referral_code, in_college, university_name, college_name, city, category, instagram, facebook, tiktok, youtube, blogs)

    db.session.add(new_registration)
    db.session.commit()


@app.route("/details", methods=["GET"])
def get_details():
    all_details = Details.query.all()
    result = detailss_schema.dump(all_details)
    return jsonify(a=result.data)

@app.route('/details/<emailid>')
def show_details(emailid):
    details = Details.query.filter_by(emailid=emailid).first_or_404()
    return details_schema.formify(details)

@app.route("/user", methods=["POST"])
def add_user():
    password = request.form['password']
    username = request.form['username']
    email = request.form['email']
    phone_no = request.form['phone_no']
    
    
    new_user = User(password, username, email, phone_no)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.formify(new_user)


@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(a=result.data)

@app.route('/user/<email>')
def show_user(email):
    user = User.query.filter_by(email=email).first_or_404()
    return user_schema.formify(user)

@app.route("/add_event", methods=["POST"])
def add_event():
    campaignid = request.form['campaignid']
    campaign_name = request.form['campaign_name']
    campaign_startdate = request.form['campaign_startdate']
    campaign_venue = request.form['campaign_venue']
    campaign_enddate = request.form['campaign_enddate']
    description = request.form['description']
    eligibility = request.form['eligibility']
    theme = request.form['theme']
    campaign_picture = request.form['campaign_picture']
    completed = request.form['completed']

    new_event = Campaign(campaignid, campaign_name, campaign_startdate, campaign_venue, campaign_enddate, description, eligibility, theme, campaign_picture, completed)

    db.session.add(new_event)
    db.session.commit()


@app.route("/event", methods=["GET"])
def get_event():
    all_events = Campaign.query.all()
    result = campaigns_schema.dump(all_events)
    return jsonify(a=result.data)


@app.route("/deleteEvent/<campaign_name>", methods=["DELETE"])
def campaign_delete(campaign_name):
    campaign = Campaign.query.filter_by(campaign_name=campaign_name).first_or_404()

    db.session.delete(campaign)
    db.session.commit()

    return campaign_schema.formify(campaign)

@app.route("/updateEvent/<campaign_name>", methods=["PUT"])
def event_update(campaign_name):
    campaign = Campaign.query.get(campaign_name)

    completed = request.form['completed']
    campaign.completed = completed

    db.session.commit()
    return user_schema.formify(campaign)