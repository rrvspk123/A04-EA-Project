
from datetime import datetime, timedelta, timezone
from hashlib import md5
from app import app, db, login
import jwt

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_posted = db.Column(db.DateTime, default=datetime.utcnow)
    followed_topics = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, followers.c.followed_id == Post.user_id
        ).filter(followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({"reset_password": self.id,
                           "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in)},
                          app.config["SECRET_KEY"], algorithm="HS256")

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")[
                "reset_password"]
        except:
            return None
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'<Search {self.search}>'




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'<Post {self.body}>'

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    link = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'<News {self.title}>'

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    link_web = db.Column(db.String(1000))
    link_p = db.Column(db.String(1000))
    title = db.Column(db.String(1000))
    middle_data = db.Column(db.String(10000))
    attributes = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class Web_tab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_w = db.Column(db.String(100))
    link_w = db.Column(db.String(1000))
    attributes = db.Column(db.String(100))
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))
    website = db.relationship('Website', backref='web_tabs')


class Website_relate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(1000))
    title_r = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class newest_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_n = db.Column(db.String(1000))
    title_n = db.Column(db.String(100))
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))

class promote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_pro = db.Column(db.String(1000))
    link_pro2 = db.Column(db.String(1000))
    title_pro = db.Column(db.String(100))

class author(db.Model):
    author_id = db.Column(db.String(100),primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))


class tags(db.Model):
    tag_id = db.Column(db.Integer,primary_key=True)
    tag = db.Column(db.String(100))
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'))

