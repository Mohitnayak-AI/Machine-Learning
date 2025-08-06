import logging

logging.basicConfig(
    filename='wed_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' # standared format to log
    )

def login(name):
    logging.info(f"User {name} logged in")
    # simulation login process
    
def process_data(data):
    try:
        # simulated data processing
        if data == 'bad_data':
            raise ValueError("Invalid Data")
        logging.info(f"Data Processing: {data}")
    except ValueError as e:
        logging.error(f'Error processing data: {e}',exc_info=True) # exc_info=True shows the line level error (more specified error ditails)
        
def logout(name):
    logging.info(f'User {name} logged out')
    
if __name__ == "__main__":
    name = "Mohit Raj Nayak"
    login(name)
    process_data("bad_data")
    logout(name)