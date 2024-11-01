import logging

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
  handlers=[logging.FileHandler("tasky.log")]
)

logger = logging.getLogger(__name__)