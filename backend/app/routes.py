from flask import jsonify
from app.models import Customer, Part, Revision, Trial, File
from app import app, db

@app.route('/api/customers')
def get_customers():
    print("Fetching customers from the database...")
    customers = Customer.query.all()
    customer_data = []

    for customer in customers:
        customer_info = {
            'name': customer.name,
            'parts': []
        }

        for part in customer.parts:
            part_info = {
                'name': part.name,
                'revisions': [],
                'trials': []
            }

            for revision in part.revisions:
                revision_info = {
                    'name': revision.name,
                    'files': [{'name': file.name} for file in revision.files]
                }
                part_info['revisions'].append(revision_info)

            for trial in part.trials:
                trial_info = {
                    'name': trial.name,
                    'files': [{'name': file.name} for file in trial.files]
                }
                part_info['trials'].append(trial_info)

            customer_info['parts'].append(part_info)

        customer_data.append(customer_info)

    print("Customers fetched successfully.")
    return jsonify(customer_data)