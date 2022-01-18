import datetime as dt

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt,
                                get_jwt_identity, set_access_cookies)

from api import blueprint as api_bp
from config import envs

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r'*': {"origins": "*"}})

JWTManager(app)
app.config['JWT_SECRET_KEY'] = envs.JWT_SECRET  # TODO: make .env
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_CSRF_IN_COOKIES'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = False
app.debug = True

app.register_blueprint(api_bp)


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = dt.datetime.now(dt.timezone.utc)
        target_timestamp = dt.datetime.timestamp(
            now + dt.timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
