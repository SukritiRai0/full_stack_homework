from flask import jsonify
from app.models import Customer, Part, Revision, Trial, File

@app.route('/api/customers')
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': customer.id, 'name': customer.name} for customer in customers])

@app.route('/api/parts')
def get_parts():
    parts = Part.query.all()
    return jsonify([{'id': part.id, 'name': part.name, 'customer_id': part.customer_id} for part in parts])

# Add similar routes for revisions, trials, and files
