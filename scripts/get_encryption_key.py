from cryptography.fernet import Fernet
from src.logger import get_logger

logger = get_logger(__name__, debug=True)
key = Fernet.generate_key()
logger.info(f"key={key}")