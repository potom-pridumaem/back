from flask import Blueprint

from .user import blueprint as user_bp

blueprint = Blueprint("discord", __name__, url_prefix="/discord")
blueprint.register_blueprint(user_bp)
