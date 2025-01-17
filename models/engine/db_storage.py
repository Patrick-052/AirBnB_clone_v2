#!/usr/bin/python3
"""Defines ``DBStorage`` class """

from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Creation of a storage clan that enables connection to the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of attributes and obtaining the environment
           to work with"""

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        # env = getenv("HBNB_ENV")

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}"
                                      + f"/{db}", pool_pre_ping=True)

        if getenv("HBNB_MYSQL_USER") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieving from the database"""

        cls_objs = {}
        inst_list = []
        if cls:
            inst_list += [cls]
        else:
            inst_list += [State, City, User, Place, Review, Amenity]
        for instance in inst_list:
            for obj in self.__session.query(instance).all():
                key = f"{type(obj).__name__}.{obj.id}"
                # del obj.__dict__["_sa_instance_state"]
                cls_objs[key] = obj
        return cls_objs

    def new(self, obj):
        """"adding a new object for the database"""
        self.__session.add(obj)

    def save(self):
        """Sending changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Doing away with an object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creation of tables and sessions"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Doing away with the current session"""
        self.__session.remove()
