"""
This file contains a function for logging messages to the terminal, enhancing visibility and traceability of events in
applications.
"""
from datetime import datetime

# Formatting constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEBUG_LEVEL_COLOR = "\033[1;34m"
SOURCE_COLOR = "\033[0;35m"
MESSAGE_COLOR = "\033[0;31m"
RESET_COLOR = "\033[0;0m"
LOG_COLOR = "\033[1;30m"


def log(debug_level: str = "", source: str = "", message: str = "") -> None:
    """
    Logs the message to the terminal
    """
    current_time = datetime.now().strftime(DATE_FORMAT)
    formatted_log = f"{LOG_COLOR}{current_time}{DEBUG_LEVEL_COLOR} {debug_level} {SOURCE_COLOR}{source}" \
                    f"{MESSAGE_COLOR} {message}{RESET_COLOR}"
    print(formatted_log, flush=True)
