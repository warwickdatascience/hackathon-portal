import random
import datetime
import time

from flask import Blueprint, request, render_template, flash
from flask import current_app as app
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename


from .models import Submission, User, Team, UserTeam

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def evaluate_score(user_score):
    return random.randint(1, 100)


# blueprint configuration
submission_bp = Blueprint("submission_bp", __name__)
# root POST request for now


@submission_bp.route("/", methods=["GET", "POST"])
# @jwt_required
def index():
    scores = [["team A", "50"], ["team B", "60"]]
    # get all user_id submissions
    submissions = [["1", "50", "LSTM"], ["2", "60", "RNN"]]
    # submissions.append(["3", "66", request.form['tag']])
    d = datetime.datetime.utcnow()
    for_js = int(time.mktime(d.timetuple())) * 1000
            
    if request.method == "POST":
        try:

            # score the user
            if 'answers' not in request.files:
                return render_template("portal.html", scores=scores,
                                   submissions=submissions,
                                   cooldown=for_js)
            file = request.files['answers']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                return render_template("portal.html", scores=scores,
                                   submissions=submissions,
                                   cooldown=for_js)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                return render_template("portal.html", scores=scores,
                                   submissions=submissions,
                                   cooldown=for_js,
                                   error="wrong")
            score = evaluate_score(file)
            # submit results
            # entry = Submission(
            #     team_id = session["team_id"],
            #     user_id = session["user_id"],
            #     score=66,
            #     tag=request.form["tag"],
            # )
            # db.session.add(entry)
            # db.session.commit()

            # get submissions where team is unique and score is maximal
            
            
        except Exception as e:
            return render_template("error.html", message=str(e))

    # otherwise, get the submission page
    scores = [["team A", "50"], ["team B", "60"]]
    submissions = [["1", "50", "LSTM"], ["2", "60", "RNN"]]
    d = datetime.datetime.utcnow()
    for_js = int(time.mktime(d.timetuple())) * 1000

    return render_template("portal.html", scores=scores,
                           submissions=submissions,

                           cooldown=for_js)
