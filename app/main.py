from fastapi import FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

from strawberry.fastapi import GraphQLRouter
from app.graphql.config import StrawberrySchema

from prometheus.config import Prometheus
""" from app.graphql.context import get_context """

graphql_app = GraphQLRouter(StrawberrySchema, graphiql=True) # , context_getter=get_context

app.include_router(graphql_app, prefix="/graphql")

Prometheus.enable(app=app)