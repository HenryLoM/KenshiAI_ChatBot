# Library
import logging

# ANSI escape codes for colors
colors = {"BLUE": "\033[94m", "YELLOW": "\033[93m", "RED": "\033[91m",
          "GRAY": "\033[90m", "RESET": "\033[0m"}

# Get the root logger (to control other modules)
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# Control logs
console_handler = logging.StreamHandler()                                        # Create a console handler
console_handler.setFormatter(logging.Formatter(colors["GRAY"] + "%(message)s"))  # Set the formatter for all logs
root_logger.addHandler(console_handler)                                          # Add the handler to the root logger
logger = logging.getLogger(__name__)                                             # Create a logger for your module


# Function to log messages
def show_up_log(message: str, level: int) -> None:
    """
    Logs a message with a custom prefix based on severity level.

    :param message: The message to log.
    :param level: An integer representing the log level (1: INFO, 2: WARNING, 3: ERROR).
    :raises ValueError: If an invalid log level is provided.
    """
    levels = {
        1: (colors["BLUE"] + "››› Info ››› ",      logger.info,    logging.INFO),
        2: (colors["YELLOW"] + "››› Warning ››› ", logger.warning, logging.WARNING),
        3: (colors["RED"] + "››› Error ››› ",      logger.error,   logging.ERROR)
    }

    if level not in levels:
        raise ValueError(f"Invalid log level: {level}. Use 1 for INFO, 2 for WARNING, or 3 for ERROR.")

    prefix, log_func, log_level = levels[level]
    log_func(f"{prefix}{message}")
