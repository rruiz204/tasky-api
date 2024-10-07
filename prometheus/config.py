from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

class Prometheus:
  @staticmethod
  def enable(app: FastAPI):
    Instrumentator().instrument(app=app).expose(app=app)