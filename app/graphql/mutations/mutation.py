import strawberry
from app.graphql.mutations.user_mutations import UserMutation

@strawberry.type
class Mutation(UserMutation):
  pass