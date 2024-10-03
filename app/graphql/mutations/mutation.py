import strawberry
from app.graphql.mutations.user_mutations import UserMutation
from app.graphql.mutations.tag_mutations import TagMutation
from app.graphql.mutations.auth_mutations import AuthMutation

@strawberry.type
class Mutation(UserMutation, TagMutation, AuthMutation):
  pass