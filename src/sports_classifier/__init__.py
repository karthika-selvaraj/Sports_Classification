import os
import sys
import logging

logFormat = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'
log_filePath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logFormat,
    handlers = [
        logging.FileHandler(log_filePath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("sportsClassifierLogger")