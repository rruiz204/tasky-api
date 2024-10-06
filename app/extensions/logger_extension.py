import logging
from strawberry.extensions import SchemaExtension

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
  handlers=[logging.FileHandler("tasky.log")]
)
logger = logging.getLogger(__name__)

class LoggerExtension(SchemaExtension):
  def on_operation(self):
    logger.info("GraphQL operation start")
    yield
    logger.info("GraphQL operation end")
  