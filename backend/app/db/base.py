from sqlalchemy.orm import DeclarativeBase

from app.models.user import User
from app.models.project import Project
from app.models.document import Document
from app.models.text import Text
from app.models.token import Token
from app.models.entity import Entity
from app.models.location import Location
from app.models.person import Person
from app.models.event import Event
from app.models.analysis import Analysis
from app.models.embedding import Embedding


class Base(DeclarativeBase):
    pass
