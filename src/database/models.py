from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from src.database.connections import Base


class BaseModelSettings(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class Worker(BaseModelSettings):
    __tablename__ = 'worker'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)


class Service(BaseModelSettings):
    __tablename__ = 'service'

    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    duration_time = Column(Float, nullable=False)


class WorkerService(BaseModelSettings):
    __tablename__ = 'worker_service'

    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    price = Column(Float, nullable=False)
    booked = Column(Boolean)
