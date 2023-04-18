from datetime import datetime
from sqlalchemy import Table,Integer,Column,String,DateTime,Float,ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


championship_user_association = Table('championship_user_association', db.Model.metadata,
    Column('championship_id', Integer, ForeignKey('championship.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)


class User(db.Model,UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(140))
    email = Column(String(140))
    password = Column(String(140))
    password_hash = Column(String(140))
    trips = db.relationship('Trip',backref='user',lazy='dynamic')
    championships = relationship('Championship', secondary=championship_user_association, back_populates='users')
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Trip(db.Model):
    id = Column(Integer, primary_key=True)
    tripname = Column(String(140))
    speed = Column(Float(precision=2),nullable=False)
    distance = Column(Float(precision=2),nullable=False)
    elevation = Column(Float(precision=2),nullable=False)
    prestige = Column(Integer,nullable=False)
    description = Column(String(140))
    recorded_on = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    score = Column(Float(precision=2),default=0.0)
    def __repr__(self):
        return '<Trip {}>'.format(self.description)

class Championship(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(140))
    start_date = Column(DateTime, index=True, default=datetime.utcnow)
    end_date = Column(DateTime, index=True, default=datetime.utcnow)
    users = relationship('User', secondary=championship_user_association, back_populates='championships')
    description = Column(String(140))
    
    def __repr__(self):
        return '<Championship {}>'.format(self.description)
