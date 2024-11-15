from app import db
from datetime import datetime

class ColumnNames:
    NAME = "name"
    NUMBER = "phone_number"
    STATUS = "status"
    CREATED_AT = "created_at"
    
class Model(db.Model):
    __tablename__ = 'Model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(15), unique=False, nullable=False)
    status = db.Column(db.Text, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
