from flask import Blueprint

from .discord import blueprint as discord_bp

blueprint = Blueprint("/api", __name__, url_prefix="/api")
blueprint.register_blueprint(discord_bp)
