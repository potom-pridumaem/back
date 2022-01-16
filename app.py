import datetime
from datetime import datetime as dt
import datetime as dt_
import os
import logging

from flask_jwt_extended import JWTManager, set_access_cookies, create_access_token, get_jwt_identity, get_jwt
from flask_cors import CORS
from flask import Flask

# from api import groups_api


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r'*': {"origins": "*"}})

JWTManager(app)
app.config['JWT_SECRET_KEY'] = CONFIG.JWT_SECRET # TODO: make .env
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_CSRF_IN_COOKIES'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = False
app.debug = True

# app.register_blueprint(groups_api.blueprint)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = dt_.datetime.now(datetime.timezone.utc)
        target_timestamp = dt_.datetime.timestamp(now + datetime.timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
