from app.database import db
from sqlalchemy.orm import relationship

class Hotel(db.Model):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    
    # Adding cascade to handle deletions and orphaned records
    reservations = relationship('app.models.reservation.Reservation', backref='hotel', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Hotel {self.name}>'
