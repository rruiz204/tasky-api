from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.user_types import CreateUserInput, UserType
from app.use_cases.user.create_user.create_user_schema import CreateUserSchena
from app.services.hasher_service import HasherService
from app.models.user import User

class CreateUserUseCase:
  def __init__(self):
    self.unitOfWork = UnitOfWork()

  def execute(self, input: CreateUserInput) -> UserType:
    validated = CreateUserSchena(**input.__dict__)

    predicate = User.email == validated.email or User.username == validated.username
    user = self.unitOfWork.users.find_user(predicate)

    if (not user is None): raise Exception("credentials in use")
    validated.password = HasherService.hash(validated.password)

    created = self.unitOfWork.users.create_user(User(**validated.model_dump()))
    return UserType(id=created.id, username=created.username, email=created.email)