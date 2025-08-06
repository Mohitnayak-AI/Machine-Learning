import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' # standared format to log
    )


logging.debug("This is a debug msg")  # lowest imp
logging.info("This is an info message")
logging.warning("This is a warning msg")
logging.error("This is an error msg")
logging.critical("This is a critical msg") # highest imp


# if we set the level as info we get all the message after info and also include info 

# in industry standard pepole usealy log it in a file (it append the new data)