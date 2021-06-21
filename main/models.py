from werkzeug.utils import validate_arguments
from secrets import token_urlsafe
from main import db

class User(db.Model):
    __tablename__ = "user"
    
    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)

    username = db.Column('USERNAME', db.String(40), nullable = False)
    # 확인해보기
    token_api = db.Column('TOKEN_API', db.String(300), nullable = False)
    token_auth = db.Column('TOKEN_USER', db.String(16), nullable = False)

    def __init__(self, name, t_api):
        self.set_username(name)
        self.set_token_api(t_api)
        self.set_token_auth('')
        
    def set_username(self, name):
        self.username = name
    
    def set_token_api(self, token):
        self.token_api = token

    def set_token_auth(self):
        self.token_auth = token_urlsafe(16)
        db.session.commit()
    
    def get_username(self):
        return self.username
    
    def get_token_api(self):
        return self.token_api

    def get_token_auth(self):
        return self.token_auth

class Repository(db.Model):
    __tablename__ = "repo"

    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)
    
    title = db.Column('TITLE', db.String(40), nullable = False)
    description = db.Column('DESCRIPTION', db.Text, nullable = False)
    name = db.Column('NAME', db.String(100), nullable = False)
    owner = db.Column('OWNER', db.ForeignKey('user.ID', ondelete='CASCADE'), nullable = False)

    def __init__(self, title, desc, name, owner):
        self.set_title(title)
        self.set_desc(desc)
        self.set_name(name)
        self.set_owner(owner)
    
    def set_title(self, title):
        self.title = title

    def set_desc(self, desc):
        self.description = desc
    
    def set_name(self, name):
        self.name = name

    def set_owner(self, owner):
        self.owner = owner
        
class Tag(db.Model):
    __tablename__ = "tag"

    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)
    
    tag_name = db.Column('TAG_NAME', db.String(40), nullable = False)
    repo = db.Column('REPO', db.ForeignKey('repo.ID', ondelete='CASCADE'), nullable = False)

    def __init(self, name, repo):
        self.set_tag_name(name)
        self.set_repo(repo)

    def set_tag_name(self, name):
        self.tag_name = name
    
    def set_repo(self, repo):
        self.repo = repo