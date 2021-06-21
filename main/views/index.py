from flask import Blueprint, redirect
from werkzeug.wrappers import PlainRequest
import config
bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('')
def index():
    return 'Index page'

@bp.route('login')
def login_test():
    return redirect("https://github.com/login/oauth/authorize?client_id="+config.GITHUB_CLIENT+"&redirect_uri=http://127.0.0.1:5000/users/logintest")#+"&scope=read:user")

# https://github.com/login/oauth/authorize?
# client_id=2a6f0b882c5a95e802c8&
# redirect_uri=http://127.0.0.1:5000/users/logintest&
# scope=public_repo