import strawberry
from app.graphql.queries.query import Query
from app.graphql.mutations.mutation import Mutation

from app.extensions.logger_extension import LoggerExtension
from app.extensions.metric_extension import MetricExtension

StrawberrySchema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[LoggerExtension, MetricExtension])