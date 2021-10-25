from ..db import db
import uuid


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.String, primary_key=True, index=True, default=lambda: str(uuid.uuid4())
    )
    username = db.Column(db.String, unique=True, index=True)
    hashed_password = db.Column(db.String)
    full_name = db.Column(db.String, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).one_or_none()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
