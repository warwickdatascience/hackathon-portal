from flask import Blueprint, request, render_template
from flask import current_app as app
from flask_jwt_extended import jwt_required
import datetime, time

# blueprint configuration
submission_bp = Blueprint("submission_bp", __name__)

# root POST request for now
@submission_bp.route("/", methods=["GET", "POST"])
# @jwt_required
def index():

    scores = [["team A", "50"], ["team B", "60"]]
    submissions = [["1", "50", "LSTM"], ["2", "60", "RNN"]]
    d = datetime.datetime.utcnow()
    for_js = int(time.mktime(d.timetuple())) * 1000

    return render_template("portal.html", scores=scores, 
        submissions=submissions,
        
        cooldown=for_js)
