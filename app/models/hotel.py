# app/models/hotel.py
from app.database import db
from sqlalchemy.orm import relationship

class Hotel(db.Model):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    # Dəyişiklik: `relationship` ilə əlaqəli modelin tam adı göstərildi
    reservations = relationship('app.models.reservation.Reservation', backref='hotel', lazy=True)

    def __repr__(self):
        return f'<Hotel {self.name}>'
