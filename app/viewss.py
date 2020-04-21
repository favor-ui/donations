from flask import jsonify, request, abort
from app import app, mongo, cur_time_and_date
from secret import *
from forms import Subscribe, Donation
#from gmail import *



@app.route('/')
def home():
    return jsonify(
        {
            "Message":"Welcome",
            "status":1
            }
            )


@app.route('/donation', methods=['POST'])
#@jwt_required
def donate():
    try:
        mongo_data = mongo.db.donations
        form = Donation(request.form)
        donated = [{"name":form.name.data}, {"email":form.email.data},{"contact":form.contact.data}, {"benefiaciaty":form.beneficiary.data}, {"amount_naira":form.amount_naira.data}, {"other_currencies":form.other_currencies.data}, {"amount_other_currencies":form.amount_other_currencies.data}, {"payment_method":form.payment_method.data}]
        
        mongo_data.insert_many(donated)
        return jsonify({"Message": "Thank you for your response!!!!. subscribe bellow to get notifications of our donation activities", "status":1})
    except Exception:
        return jsonify({"Message":"Sorry you are not eable to donate now, you could try later"})


@app.route('/donations/donors', methods=['GET'])
def get_donors_names():
    try:
        mongo_data = mongo.db.donations
        find_names = mongo_data.find()
        for name in find_names:
            return jsonify({"Donors":"name"})
    except Exception:
        return jsonify({"Message":"Something went wrong  Please check"})


@app.route('/donations/donors_details', methods=['GET'])
@jwt_required
def get_donors_details():
    try:
        mongo_data = mongo.db.donations
        document = mongo_data.find()
        for donation in document:
            return jsonify({"Donation Details": donation})
    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})



@app.route('/subscribe', methods=['POST'])
@JWT_SECRET_KEY
def sub():
    try:
        mongo_data = mongo.db.mailing_lists
        form = Subscribe(request.form)
        mailing_list = [{"name":form.name.data}, {"email":form.email.data}]
        
        email=form.email.data
        find_email = mongo_data.find_one({"email":email})
        
        if find_email:
            return jsonify({"Error":"User exist", "status":0})
        else:
            mongo_data.insert_many(mailing_list)
            return jsonify({"Message": "You can now get updates on our activites directly in your mail box", "status":1})
    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})



@app.route('/subscribe/emai_list', methods=['GET'])
@jwt_required
def get_donors_details():
    try:
        mongo_data = mongo.db.mailing_lists
        mails = mongo_data.find()
        for subscribers in mails:
            return jsonify({"All Subscribers": subscribers})
    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})





@app.errorhandler(400)
def bad_request__error(exception):
    return jsonify(
        {
            "Message": "Sorry you entered wrong values kindly check and resend!"
        },
        {
            "status":400
        }
    )


@app.errorhandler(401)
def internal_error(error):
    return jsonify(
        {
            "Message": "Acess denied ! please register and login to generate API KEY"
        },
        {
            "status": 401
        }
    )



@app.errorhandler(404)
def not_found_error(error):
    return jsonify(
        {
            "Message":"Sorry the page your are looking for is not here kindly go back"
        },
        {
            "status": 404
        }
    )





@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        {
            "Message": "Sorry the requested method is not allowed kindly check and resend !"
        },
        {
            "status": 405
        }
    )

@app.errorhandler(500)
def method_not_allowed(error):
    return jsonify(
        {
            "Message": "Bad request please check your input and resend !"
        },
        {
            "status": 500
        }
    )

