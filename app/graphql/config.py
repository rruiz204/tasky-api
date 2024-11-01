import strawberry
from app.graphql.queries.query import Query
from app.graphql.mutations.mutation import Mutation

StrawberrySchema = strawberry.Schema(query=Query, mutation=Mutation)