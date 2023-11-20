from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import httpx

from amazon import AmazonScraper
from snapdeal import SnapdealScraper

app = Flask(__name__)
#app.config['MONGO_URI'] = 'your_mongo_db_uri'
#mongo = PyMongo(app)


def compare_prices(search_term, filter_type, top_n, comparison_websites):
    # Initialize an empty list to store scraped data

    result = []

    # Dictionary to map websites to scraper classes
    website_scraper_mapping = {
        'amazon': AmazonScraper,
        'snapdeal': SnapdealScraper,

        # Add more mappings for other comparison websites as needed
    }
    print("in func")

    for website in comparison_websites:
        # Check if the scraper class exists for the given website
        if website.lower() in website_scraper_mapping:
            # Instantiate the appropriate scraper class
            scraper_class = website_scraper_mapping[website.lower()]
            scraper = scraper_class()

            # Perform web scraping using the chosen scraper
            scraped_data = scraper.scrape(search_term, filter_type, top_n)

            # Add the scraped data to the result list in the desired format
            result.extend([{
                'title': product['title'],
                'url': product['url'],

                'rating': product['rating'],
                'price': product['price'],
                'website': website
            } for product in scraped_data])

    # Calculate total products considered
    total_products_considered = len(result)

    print(result)

    # Construct the final API output
    api_output = {
        'products': result,
        'total_products_considered': total_products_considered
    }

    return api_output
@app.route('/api/compare_prices', methods=['POST'])
def api_compare_prices():
    # Get input parameters from the request
    search_term = request.json.get('searchTerm', '')
    filter_type = request.json.get('filter', 'none')
    top_n = request.json.get('topN', 3)
    comparison_websites = request.json.get('websites', [])

    print(search_term)
    print(filter_type)
    print(top_n)
    print(comparison_websites)

    # Implement web scraping logic in web_scraper.py

    result = compare_prices(search_term, filter_type, top_n, comparison_websites)
    print(result)

    return jsonify(result)

    # return "a dummy response"

@app.route('/')
def index():
    return render_template('index.html')


# from app.routes import main_bp
#
# # Register the blueprint with the app
# app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run(debug=True)

