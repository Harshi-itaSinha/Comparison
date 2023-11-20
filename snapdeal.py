import requests
from bs4 import BeautifulSoup

class SnapdealScraper:
    def scrape(self, search_term, filter_type, top_n):
        # URL for Snapdeal search results
        top_n = int(top_n)
        url = f'https://www.snapdeal.com/search?keyword={search_term}&sort={filter_type}'

        # Send a GET request to the Snapdeal search results page
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information based on your needs
            product_data = []

            # Example: Extracting product details (title, price, rating, URL)
            products = soup.select('.product-desc-rating')
            for product in products[:top_n]:
                title = product.select_one('.product-title').text.strip()
                price = product.select_one('.product-price').text.strip()

                # Check for the presence of the rating element
                rating_element = product.select_one('.filled-stars')
                rating_style = rating_element['style'] if rating_element else 'N/A'

                # Remove the 'width' attribute and convert percentage to stars
                rating_percentage = rating_style.split(':')[1].replace('%', '')
                stars = round(float(rating_percentage) / 20, 1) if rating_percentage else 'N/A'

                product_url = product.find('a', {'class': 'dp-widget-link'})['href']  # Extracting URL

                # Storing data in a dictionary
                product_info = {
                    'title': title,
                    'price': price,
                    'rating': stars,
                    'url': product_url
                }
                product_data.append(product_info)

            return product_data
        else:
            print(f"Failed to retrieve data from Snapdeal. Status code: {response.status_code}")
            return []

# Example usage:
# snapdeal_scraper = SnapdealScraper()
# snapdeal_data = snapdeal_scraper.scrape('laptop', 'relevance', 3)
# print(snapdeal_data)
