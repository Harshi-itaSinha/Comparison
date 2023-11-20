# app/routes.py
from flask import Blueprint, render_template, jsonify
from flask_pymongo import PyMongo

# Create a Blueprint instance
main_bp = Blueprint('main', __name__)

# Create a PyMongo instance
# mongo = PyMongo()
print(",check in routes")

@main_bp.route('/')
def index():
    print("in routes")
    return render_template('index.html')


@main_bp.route('/api/compare_prices', methods=['POST'])
def compare_prices():
    # Implement the price comparison logic here
    # Use request.json to access the JSON data from the request

    # Placeholder response for demonstration
    print("here is the response")

    result = {
        'products': [{
            'title': 'Sample Product',
            'url': 'https://example.com',
            'total_review_count': '100',
            'rating': '5',
            'price': '100',
            'website': 'https://example.com'
        }],
        'total_products_considered': 1
    }
    return jsonify(result)
