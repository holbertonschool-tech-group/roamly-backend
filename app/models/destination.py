from app.database import db
from sqlalchemy.orm import relationship

class Destination(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Establishing a relationship with the Hotel model and cascading deletions
    hotels = relationship('app.models.hotel.Hotel', backref='destination', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Destination {self.name}>'
