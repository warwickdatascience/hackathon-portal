from flask import Blueprint, request, render_template, redirect
from flask import current_app as app
from flask_jwt_extended import jwt_optional, get_jwt_identity
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from .models import Submission, User, UserTeam, Team
from .score import evaluate_score
from . import db
import datetime, time
import os

# blueprint configuration
submission_bp = Blueprint("submission_bp", __name__)
# root POST request for now


@submission_bp.route("/", methods=["GET", "POST"])
@jwt_optional
def index():
    username = get_jwt_identity()
    user_id = User.query.filter_by(username=username).first().user_id
    team_id = UserTeam.query.filter_by(user_id=user_id).first().team_id
    team_name = Team.query.filter_by(team_id=team_id).first().teamname

    # username is None if not logged in
    # redirect if this is the case
    if username is None:
        return redirect("/login")

    if request.method == "POST":
        csv_file = request.files["cFile"]
        jupyter_file = request.files["jFile"]
        # check extensions
        csv_filename = csv_file.filename
        jupyter_filename = jupyter_file.filename
        if "." in csv_filename and csv_filename.rsplit(".", 1)[1].lower() == "csv" and "." in jupyter_filename and jupyter_filename.rsplit(".", 1)[1].lower() == "ipynb":
            csv_filename = secure_filename(csv_file.filename)
            jupyter_filename = secure_filename(jupyter_file.filename)

            # save the files to the upload folder
            # get the id to give them
            new_submission = Submission(team_id=team_id, user_id = user_id, upload_time=datetime.datetime.utcnow(), tag=request.form["tag"])

            db.session.add(new_submission)
            db.session.flush()

            csv_file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"{new_submission.submission_id}.csv"))
            jupyter_file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"{new_submission.submission_id}.ipynb"))

            # call the score function
            new_submission.score = evaluate_score(os.path.join(app.config["UPLOAD_FOLDER"], f"{new_submission.submission_id}.csv"))

            db.session.add(new_submission)
            db.session.commit()
            return redirect("/")

        return "Bad file extensions used"
        
    scores = [["team A", "50"], ["team B", "60"]]
    submissions = [["1", "50", "LSTM"], ["2", "60", "RNN"]]

    potential_d = Submission.query.filter_by(team_id=team_id).order_by(desc(Submission.upload_time)).first()

    if potential_d is None:
        d = datetime.datetime.utcnow()
    else:
        d = potential_d.upload_time


    for_js = (d - datetime.datetime(1970,1,1,0,0,0)).total_seconds() * 1000
    return render_template("portal.html",
            team_name=team_name,
            scores=scores,submissions=submissions,cooldown=for_js)
