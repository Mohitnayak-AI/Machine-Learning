import logging

logging.basicConfig(level=logging.INFO)


logging.debug("This is a debug msg")  # lowest imp
logging.info("This is an info message")
logging.warning("This is a warning msg")
logging.error("This is an error msg")
logging.critical("This is a critical msg") # highest imp


# if we set the level as info we get all the message after info and also include info 