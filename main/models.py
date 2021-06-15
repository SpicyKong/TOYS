from main import db

class User(db.Model):
    __tablename__ = "user"
    
    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)

    username = db.Column('USERNAME', db.String(40), nullable = False)
    # 확인해보기
    token_api = db.Column('TOKEN_API', db.String(300), nullable = False)
    token_auth = db.Column('TOKEN_USER', db.String(16), nullable = False)

class Repository(db.Model):
    __tablename__ = "repo"

    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)
    
    title = db.Column('TITLE', db.String(40), nullable = False)
    description = db.Column('DESCRIPTION', db.String(1000), nullable = False)
    name = db.Column('NAME', db.String(100), nullable = False)
    owner = db.Column('OWNER', db.ForeignKey('user.ID', ondelete='CASCADE'), nullable = False)

class Tag(db.Model):
    __tablename__ = "tag"

    # 기본키
    id = db.Column('ID', db.Integer, primary_key=True, nullable = False)
    
    value = db.Column('VALUE', db.String(40), nullable = False)
    repo = db.Column('REPO', db.ForeignKey('repo.ID', ondelete='CASCADE'), nullable = False)
