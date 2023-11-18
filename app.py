from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import httpx

app = Flask(__name__)
#app.config['MONGO_URI'] = 'your_mongo_db_uri'
#mongo = PyMongo(app)

# MongoDB Schema
# class Product(mongo.Document):
#     title = mongo.StringField()
#     url = mongo.StringField()
#     total_review_count = mongo.StringField()
#     rating = mongo.StringField()
#     price = mongo.StringField()
#     website = mongo.StringField()

# API endpoint
# @app.route('/api/compare_prices', methods=['POST'])
# def compare_prices():
#     search_term = request.json.get('search_term')
#     filter_type = request.json.get('filter_type', 'none')
#     top_n = int(request.json.get('top_n', 3))
#     comparison_websites = request.json.get('comparison_websites', [])
#
#     # TODO: Implement price comparison logic using httpx and update MongoDB
#     # Placeholder code below
#     # result = {
#     #     'products': Product.objects[:top_n].to_json(),
#     #     'total_products_considered': min(top_n, Product.objects.count())
#     # }
#     # return jsonify(result)
#
# # Web interface route
# @app.route('/')
# def index():
#     return render_template('index.html')


from app.routes import main_bp

# Register the blueprint with the app
app.register_blueprint(main_bp)

if __name__ == '__main__':
    print("just here")
    app.run(debug=True)

