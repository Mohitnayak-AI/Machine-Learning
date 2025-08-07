import logging

def setup_log(name):
    # create a custom log
    logger = logging.getLogger(name)

    # configer log
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('/Users/mohitrajnayak/Data Sci Work/Data Sci REPO/Machine-Learning/AI-codebasics/project/backend/db_helper_log.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger