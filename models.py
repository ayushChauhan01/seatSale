from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    place = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    bookings = db.relationship('Booking', backref='show', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# This model defines four database tables: User, Venue, Show, and Booking. The User table stores user
# information, including their username, password, and bookings. The Venue table stores information about
# the venues, including their ID, name, place, and capacity, and also has a one-to-many relationship with
# the Show table. The Show table stores information about the shows, including their ID, name, rating, 
# tags, ticket price, and the ID of the venue where the show is being held. The Show table also has a 
# one-to-many relationship with the Booking table. Finally, the Booking table stores information about 
# each booking, including the ID of the user who made the booking, the ID of the show being booked, the 
# number of tickets, and the booking date.