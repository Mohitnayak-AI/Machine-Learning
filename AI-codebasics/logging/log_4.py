import logging

# create a custom logger
logger = logging.getLogger("my_logs")

# configer the custom logger
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('my_custom.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#logging Massage
logger.debug("This is a debug msg")
logger.info("This is an info message")
logger.warning("This is a warning msg")
logger.error("This is an error msg")
logger.critical("This is a critical msg")