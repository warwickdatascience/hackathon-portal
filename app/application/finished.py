from flask_login import login_required, current_user
from flask import Blueprint, request, render_template, redirect
from flask import current_app as app

from flask_jwt_extended import jwt_optional, get_jwt_identity
from flask_login import login_required, current_user
from sqlalchemy import desc, func
from werkzeug.utils import secure_filename
from .models import Submission, User, UserTeam, Team
from .score import evaluate_score
from . import db
import datetime, time
import os


def get_scores():
    scores = db.session.query(Submission.team_id, func.max(Submission.score)).group_by(Submission.team_id).order_by(func.max(Submission.score).desc()).all()

    # can't be asked to look up SQLAlchemy joins
    scores_names = list()
    for (teamid, score) in scores:
        scores_names.append((Team.query.filter_by(team_id=teamid).first().teamname, score))

    return sorted(scores_names, key=lambda x : x[1])


# blueprint configuration
finished_bp = Blueprint("finished_bp", __name__)

@finished_bp.route('/thankyou', methods=['GET', 'POST'])
# @login_required
def finished():
    # if global countdown not over 
    d = datetime.datetime.utcnow()
    end_date = datetime.datetime.strptime('Nov 15 2020 7:00PM', '%b %d %Y %I:%M%p')
    # if d < end_date:
    #     return redirect("/")
    user_id = User.query.filter_by(username=current_user.username).first().user_id
    team_id = UserTeam.query.filter_by(user_id=user_id).first().team_id
    team_name = Team.query.filter_by(team_id=team_id).first().teamname
    return render_template('thankyou.html', username=current_user.username, team_name=team_name, scores=get_scores())

