from flask import Blueprint, request
from flask import current_app as app

# blueprint configuration
submission_bp = Blueprint("submission_bp", __name__)

# root POST request for now
@submission_bp.route("/", methods=["GET", "POST"])
def index():
    return "Hello world"
