from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Runa(Base):
    __tablename__ = "runas"

    id = Column(Integer, primary_key=True, index=True)
    main = Column(String, index=True)
    description = Column(String, index=True)
    equipada = Column(Boolean, default=True)
