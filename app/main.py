from fastapi import FastAPI
app = FastAPI()

from strawberry.fastapi import GraphQLRouter
from app.graphql.config import StrawberrySchema

from prometheus.config import Prometheus
""" from app.graphql.context import get_context """

graphql_app = GraphQLRouter(StrawberrySchema, graphiql=True) # , context_getter=get_context

app.include_router(graphql_app, prefix="/graphql")

Prometheus.enable(app=app)