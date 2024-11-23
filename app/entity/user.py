from app.database import db
from sqlalchemy.orm import relationship
from app.entity.base_entity import BaseEntity

class User(BaseEntity, db.Model):  # BaseEntity sinifindən miras alınır
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # reservations = relationship('Reservation', backref='user', lazy=True)
    # blog_posts = relationship('BlogPost', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
