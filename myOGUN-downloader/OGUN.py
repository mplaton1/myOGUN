"""
Module for OGUN class.
"""
from typing import Dict
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from .utils import get_group_id, get_week_day, get_start_time, get_end_time



Base = declarative_base()

class OGUN(Base):
    """
    Class containing all important information about OGUN.
    It uses ORM for convenience.
    """
    @classmethod
    def ogun_builder(cls, data: Dict[str, str]):
        """
        Constructor of OGUN from dictionary. Dictionary must be valid.
        :param data:
        :return: OGUN
        """
        return OGUN(link=data.get("link"),
                    ects=data.get("Punkty ECTS"),
                    adress=data.get("Miejsce"),
                    date_of_lessons=data.get("Termin"),
                    ogun_group_id=get_group_id(data.get("link")),
                    hours_number=data.get("Liczba godzin"),
                    date_week_day=get_week_day(data.get("Termin")),
                    start_time=get_start_time(data.get("Termin")),
                    end_time=get_end_time(data.get("Termin")))

    def has_all_fields(self) -> bool:
        """
        Checks whether all fields of class instance are set(not None).
        :return: bool
        """
        result = True
        for attr in self.__dict__:
            if self.__dict__.get(attr) is None:
                result = False
        return result

    __tablename__ = 'ogun'
    id = Column(Integer, primary_key=True)
    link = Column(String)
    ects = Column(Integer)
    adress = Column(String)
    hours_number = Column(Integer)
    date_of_lessons = Column(String)
    ogun_group_id = Column(String, nullable=False)
    date_week_day = Column(String)
    start_time = Column(String)
    end_time = Column(String)
