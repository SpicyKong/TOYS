from flask import Blueprint
from flask.helpers import make_response
import config, requests, jwt
from flask.globals import request
from main.models import User
from main import db
from time import time
bp_users = Blueprint('users', __name__, url_prefix='/users')

@bp_users.route('', methods=["POST"])
def auth():
    print('chk')
    return 'Index page'


@bp_users.route('/logintest')
def logintest():
    code = request.args.get('code', None)
    if code is None:
        return make_response({'message':'추후상태코드설정'}, 400)
    url = "https://github.com/login/oauth/access_token?client_id="+config.GITHUB_CLIENT+'&client_secret='+config.GITHUB_SECRET+"&code="+code
    
    header = { 'Accept':'application/vnd.github.v3+json' }
    res = requests.get(url, headers=header).json()
    access_token = res['access_token'] if 'access_token' in res else None
    
    if access_token is None:
        return make_response({'message':'추후상태코드설정'}, 400)
        
    #header['Accept'] = 'application/vnd.github.v3+json'
    header['Authorization'] = "token "+access_token
    user_info = requests.get("https://api.github.com/user", headers=header).json()
    #print(res)
    #print(user_name['login'])
    user = db.session.query(User).filter_by(username=user_info['login']).first()
    if user is None:
        user = User(name=user_info['login'], t_api=access_token)
        db.session.add(user)
        db.session.commit()
    user.set_token_auth()
    
    token_info = {
        'expiration':(int(time())+7200),
        'username':user_info['login'],
    }
    
    user_token = jwt.encode(token_info, user.get_token_auth(), algorithm='HS256')
    ret = make_response({'message':'로그인 성공'}, 200)
    ret.set_cookie('user_token', user_token, httponly=True)
    print(user_token)
    return ret




"""
        to do:
        1. 얻은 액세스 토큰으로 어떤 유저인지 특정하기
        2. 해당 유저가 db에 있는지 조회
            - 없다면 새로 만듬
        3. 유저의 액세스 토큰을 저장
        4. 유저에게 jwt 발급
        5. 로그아웃시 토큰 삭제 및 salt 갱신

        프로젝트 등록
        1. 요청이 들어오면 jwt를 검증함
        2. 검증 성공시 어떤 유저인지 특정함.
        3. 요청한 내용대로 리포지토리를 등록함.
        4. 해시태그가 있다면 입력 받은 해시태그를 잘 분리한 후 리포지토리, 태그명을 이용해 저장
        (프로젝트 컬럼에 스타 수, 날짜도 넣어서 정렬할때 이용하자.)

        프로젝트 삭제
        1. 요청이 들어오면 그냥 삭제함.
        (차피 cascade 옵션때문에 알아서 다 삭제될 듯)

        페이징
        

    
"""