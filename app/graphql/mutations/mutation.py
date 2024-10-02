import strawberry
from app.graphql.mutations.user_mutations import UserMutation
from app.graphql.mutations.tag_mutations import TagMutation

@strawberry.type
class Mutation(UserMutation, TagMutation):
  pass