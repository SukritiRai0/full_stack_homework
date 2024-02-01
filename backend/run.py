import logging
from app import create_app, db
from sqlalchemy.exc import OperationalError
from retry import retry
import sys
# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Define the create_tables function with retry logic
@retry(OperationalError, delay=16)
def create_tables():
    logging.info('Creating database tables...')
    db.create_all()
    logging.info('Database tables created.')
if __name__ == '__main__':
    logging.info('Creating Flask app...')
    app = create_app()  # Create the Flask app
    with app.app_context():
        create_tables()  # Create database tables within the app context
    logging.info('Starting Flask app...')
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the app
