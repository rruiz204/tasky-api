from app.services.logger_service import logger
from strawberry.extensions import SchemaExtension

class LoggerExtension(SchemaExtension):
  def on_operation(self):
    logger.info(self.execution_context.query)
    yield
  