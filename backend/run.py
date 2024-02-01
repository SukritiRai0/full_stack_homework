import logging
from app import create_app, db
from sqlalchemy.exc import OperationalError  # Import OperationalError
from retry import retry 

import sys

# Configure logging to output to stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    # Retry creating the app with the database connection
    logging.info('Creating Flask app...')
    with create_app().app_context():
        # Retry creating database tables
        @retry(OperationalError, delay=1, backoff=2, max_delay=16)
        def create_tables():
            logging.info('Creating database tables...')
            db.create_all()
            logging.info('Database tables created.')

        create_tables()

    logging.info('Starting Flask app...')
    create_app().run(host='0.0.0.0', port=5000, debug=True)
