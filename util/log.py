import logging

# ANSI escape codes for colors
RESET = "\033[0m"
COLORS = {
    "DEBUG": "\033[94m",   # Blue
    "INFO": "\033[92m",    # Green
    "WARNING": "\033[93m", # Yellow
    "ERROR": "\033[91m",   # Red
    "CRITICAL": "\033[95m" # Magenta
}

# Custom formatter to apply color to log messages based on log level
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Get the log level name (DEBUG, INFO, etc.) and apply the corresponding color
        log_color = COLORS.get(record.levelname, RESET)
        
        # Format the original log message with the color
        formatted_message = super().format(record)
        return f"{log_color}{formatted_message}{RESET}"

# Custom log format
FORMAT = "%(asctime)s %(levelname)s: [%(filename)s - %(funcName)s] %(message)s"

# Create a handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Set the custom formatter to the handler
formatter = CustomFormatter(FORMAT)
handler.setFormatter(formatter)

# Get the logger and apply the handler
logger = logging.getLogger("CTOntoLib")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
