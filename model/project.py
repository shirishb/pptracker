from model import *

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.types import String, Integer, Date, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import CheckConstraint

# todo help text
PROJECT_TYPE = {
    "book": "",
    "coding" : "",
}

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    tag = Column(String(40), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    date_started = Column(Date)
    date_finished = Column(Date)
    priority = Column(Integer, default=0, nullable=False)
    type = Column(Enum(*PROJECT_TYPE.keys(), name="cst_project_type"), nullable=False)
    isbn = Column(String(20))
    activities = relationship("Activity", backref="project")

    __table_args__ = (
        CheckConstraint(CONSTRAINT_PRIORITY, name="cst_priority"),
        CheckConstraint(CONSTRAINT_DATE_BEFORE.format("date_started"), name="cst_date_started"),
        CheckConstraint(CONSTRAINT_DATE_BEFORE.format("date_finished"), name="cst_date_finished"),
        CheckConstraint(CONSTRAINT_STRING_LOWER.format("tag"), name="cst_tag_lower"),
    )

    def __init__(self, tag, name, priority):
        self.tag = tag
        self.name = name
        self.priority = priority

    def set_date(started=None, finished=None):
        if started:
            self.date_started = started
        if finished:
            self.date_finished = finished
            # finished on same day
            if not started:
                self.date_started = finished

    def set_type(type, **kwargs):
        self.type = type

    def __repr__(self):
        return "Project(id=%r, tag=%r, name=%r, started=%r, priority=%r)" % \
            (self.id, self.tag, self.name, self.date_started, self.priority)

