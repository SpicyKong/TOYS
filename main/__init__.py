from flask import Flask

import config

# db를 위한 모듈들
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    
    # 앱 초기 설정
    app.config.from_object(config)
    app.config['JSON_AS_ASCII'] = False
    app.secret_key = config.MY_SALT

    # 앱 DB 설정
    db.init_app(app)
    migrate.init_app(app, db)
    
    bcrypt.init_app(app)

    from . import models
    from .views import index, users
    app.register_blueprint(index.bp)
    app.register_blueprint(users.bp_users)
    return app