import requests
from bs4 import BeautifulSoup

class AmazonScraper:
    def scrape(self, search_term, filter_type, top_n):
        # URL for Amazon search results
        url = f'https://www.amazon.in/s?k={search_term}&sort={filter_type}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        top_n=int(top_n)

        response = requests.get(url, headers=headers)


        # Send a GET request to the Amazon search results page


        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information based on your needs
            product_data = []

            # Example: Extracting product details (title, price, rating, URL)
            products = soup.select('.s-result-item')
            for product in products[:top_n]:
                title_element = product.select_one('span.a-size-medium.a-color-base.a-text-normal')
                title = title_element.text.strip() if title_element else 'N/A'

                price_element = product.select_one('.a-offscreen')
                price = price_element.text.strip() if price_element else 'N/A'

                # Check for the presence of the rating element
                rating_element = product.select_one('.a-icon-star-small')
                rating = rating_element.find_next('span').text if rating_element else 'N/A'

                product_url_element = product.find('a', {'class': 'a-link-normal'})
                product_url = f'https://www.amazon.in{product_url_element["href"]}' if product_url_element else 'N/A'

                # Storing data in a dictionary
                product_info = {
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'url': product_url
                }
                product_data.append(product_info)

            return product_data

        else:
            print(f"Failed to retrieve data from Amazon. Status code: {response.status_code}")
            return []

# Example usage:
# amazon_scraper = AmazonScraper()
# amazon_data = amazon_scraper.scrape('laptop', 'price-asc-rank', 3)
# print(amazon_data)
