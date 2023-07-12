import logging 
import os
from datetime import datetime

# file to be saved in the name of datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# path where log files has to be generated
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# even though there are files, keep appending the files to the same directory.
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging has started")