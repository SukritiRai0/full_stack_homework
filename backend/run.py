from app import create_app, db
from sqlalchemy.exc import OperationalError  # Import OperationalError
from retry import retry 

if __name__ == '__main__':
    # Retry creating the app with the database connection
    with create_app().app_context():
        # Retry creating database tables
        @retry(OperationalError, delay=1, backoff=2, max_delay=16)
        def create_tables():
            db.create_all()

        create_tables()

    create_app().run(host='0.0.0.0', port=5000, debug=True)
