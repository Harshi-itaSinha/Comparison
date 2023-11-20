import requests
from bs4 import BeautifulSoup

class MeeshoScraper:
    def scrape(self, search_term, filter_type, top_n):
        # URL for Meesho search results
        url = f'https://meesho.com/search/{search_term}?sort={filter_type}'

        # Send a GET request to the Meesho search results page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)



        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information based on your needs
            product_data = []

            # Example: Extracting product details (title, price, rating, URL)
            products = soup.select('.product-card')
            for product in products[:top_n]:
                title_element = product.select_one('.product-title')
                title = title_element.text.strip() if title_element else 'N/A'

                price_element = product.select_one('.product-price')
                price = price_element.text.strip() if price_element else 'N/A'

                # Extracting product rating (if available)
                rating_element = product.select_one('.product-rating')
                rating = rating_element.text.strip() if rating_element else 'N/A'

                # Extracting product URL
                product_url_element = product.find('a', {'class': 'product-link'})
                product_url = product_url_element['href'] if product_url_element else 'N/A'

                # Storing data in a dictionary
                product_info = {
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'product_url': f'https://meesho.com{product_url}'  # Make the URL absolute
                }
                product_data.append(product_info)

            return product_data

        else:
            print(f"Failed to retrieve data from Meesho. Status code: {response.status_code}")
            return []

# Example usage:
meesho_scraper = MeeshoScraper()
meesho_data = meesho_scraper.scrape('laptop', 'relevance', 3)
print(meesho_data)
