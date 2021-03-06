from model import *

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.types import String, Integer, Date, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import CheckConstraint

# todo help text
ACTIVITY_TYPE = {
    "pages" : "",
    "problems" : "",
    "http_url" : "",
}

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    description = Column(String(80), nullable=False)
    date_started = Column(Date)
    date_finished = Column(Date)
    priority = Column(Integer, default=0, nullable=False)
    type = Column(Enum(*ACTIVITY_TYPE.keys(), name="cst_activity_type"), nullable=False)
    int_data = Column(Integer)
    string_data = Column(String(255))
    date_planned = Column(Date)
    estimated_days = Column(Integer)

    __table_args__ = (
        CheckConstraint(CONSTRAINT_PRIORITY, name="cst_priority"),
        CheckConstraint(CONSTRAINT_DATE_BEFORE.format("date_started"), name="cst_date_started"),
        CheckConstraint(CONSTRAINT_DATE_BEFORE.format("date_finished"), name="cst_date_finished"),
        CheckConstraint(CONSTRAINT_DATE_AFTER.format("date_planned"), name="cst_date_planned"),
        CheckConstraint(CONSTRAINT_UNSIGNED_INTEGER.format("estimated_days"), name="cst_estimated_days"),
    )

    def __repr__(self):
        return "Activity(id=%r, project_id=%r, started=%r, priority=%r)" % \
            (self.id, self.project_id, self.date_started, self.priority)

