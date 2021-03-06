import uuid

from ..db import db


class User(db.Model):
    __tablename__ = "users"

    # If DB is PostgreSQL preferred to use smth like this:
    #     from sqlalchemy.dialects.postgresql import UUID
    #     id = db.Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    # But current variant universal for all SQL DBs
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

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "is_active": self.is_active,
        }
