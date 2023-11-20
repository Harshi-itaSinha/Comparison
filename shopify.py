import requests
from bs4 import BeautifulSoup

class AjioScraper:
    def scrape(self, search_term, filter_type, top_n):
        # URL for Ajio search results
        url = f'https://www.ajio.com/search/?text={search_term}'

        # Send a GET request to the Ajio search results page
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information based on your needs
            # Example: Extracting product details (modify as needed)
            products = soup.select('.rilrtl-products-list__item')
            print(soup)

            scraped_data = []
            for product in products[:top_n]:
                title = product.select_one('.nameCls').text.strip()
                price = product.select_one('.price').text.strip()
                url = product.select_one('.rilrtl-products-list__link')['href']
                rating = None  # Adjust the selector based on the actual HTML structure
                # Add more information extraction as needed

                # Store the data in a dictionary
                product_data = {
                    'title': title,
                    'price': price,
                    'url': f'https://www.ajio.com{url}',  # Complete the relative URL
                    'rating': rating.text.strip() if rating else 'N/A',  # Check if rating is available
                    # Add more fields as needed
                }

                scraped_data.append(product_data)

            return scraped_data

        else:
            print(f"Failed to retrieve data from Ajio. Status code: {response.status_code}")
            return []

# Example usage:
ajio_scraper = AjioScraper()
ajio_data = ajio_scraper.scrape('rucksack', 'relevance', 3)
print(ajio_data)
