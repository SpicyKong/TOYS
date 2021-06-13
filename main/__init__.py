from flask import Flask

import config


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(config)
    app.config['JSON_AS_ASCII'] = False
    app.secret_key = config.MY_SALT

    return app