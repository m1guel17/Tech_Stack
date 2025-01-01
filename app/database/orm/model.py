from app import db

from datetime import datetime

class Model(db.Model):
    __tablename__ = 'Model'

    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(25), nullable=True)
    integer = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.String(12), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

class ModelBuilder:
    def __init__(self):
        self._string = None
        self._integer = None
        self._phone_number = None
        self._created_at = None
    
    def set_string(self, string: str):
        self._string = string
        return self

    def set_integer(self, integer: int):
        self._integer = integer
        return self

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number
        return self

    def set_created_at(self, created_at: datetime):
        self._created_at = created_at
        return self

    # Create a new instance
    def build(self) -> Model:
        return Model(
            string=self._string,
            integer=self._integer,
            phone_number=self._phone_number,
            created_at=self._created_at if self._created_at else datetime.now()
        )
