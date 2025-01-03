from app.database import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to User and Hotel models
    user = db.relationship('User', backref='reservations')
    hotel = db.relationship('Hotel', backref='reservations')

    def __repr__(self):
        return f'<Reservation {self.id}>'

    # Additional utility methods (e.g., validation) can be added here
    def is_valid(self):
        """ Checks if the reservation is valid (check-in < check-out) """
        return self.check_in < self.check_out
