from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from init import db

# Comments
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment: Mapped[str] = mapped_column(String)