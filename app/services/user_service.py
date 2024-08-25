from typing import List
from app.graphql.schema.user import UserType, UserInput
from app.validations.user import UserInputModel
from app.services.data import users

def get_all_users() -> List[UserType]:
  return [UserType(**user) for user in users]

def get_specific_user(user_id: int) -> UserType:
  user = list(filter(lambda user: user["id"] == user_id, users))
  if (not user): raise ValueError(f"User with id {user_id} not found")
  return UserType(**user[0])

def create_user(input: UserInput) -> UserType:
  valid = UserInputModel(username=input.username, email=input.email, password=input.password)
  
  new_id = max(user["id"] for user in users) + 1 if users else 1
  new_user = {
    "id": new_id,
    "username": valid.username,
    "email": valid.email,
    "password": valid.password
  }
  users.append(new_user)
  return UserType(**new_user)