from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from datetime import datetime
from typing import List
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    image_file: Mapped[str] = mapped_column(
        String(20), nullable=False, default="default.jpg")

    posts: Mapped[List["Post"]] = relationship(
        back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    date_posted: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
