import requests
from bs4 import BeautifulSoup


class FlipkartScraper:
    def scrape(self, search_term, filter_type, top_n):
        # URL for Flipkart search results
        #url = f'https://www.flipkart.com/search?q={search_term}'
        url='https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
        }

        response = requests.get(url, headers=headers)

        # Send a GET request to the Flipkart search results page


        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response, 'html.parser')
            # Extract relevant information based on your needs
            title = soup.select_one('._4rR01T').text.strip()
            rating = soup.select_one('._1lRcqv .hGSR34').text.strip()
            reviews = soup.select_one('._1lRcqv ._13vcmD').text.strip()
            price = soup.select_one('._30jeq3').text.strip()
            discounted_price = soup.select_one('._3I9_wc').text.strip()
            discount_percentage = soup.select_one('._3Ay6Sb span').text.strip()
            delivery_info = soup.select_one('._3tcB5a .p8ucoS').text.strip()

            product_info = {
                'title': title,
                'rating': rating,
                'reviews': reviews,
                'price': price,
                'discounted_price': discounted_price,
                'discount_percentage': discount_percentage,
                'delivery_info': delivery_info
            }

            return product_info
        else:
            print(f"Failed to retrieve data from Flipkart. Status code: {response.status_code}")
            return []

# Example usage:
flipkart_scraper = FlipkartScraper()
flipkart_data = flipkart_scraper.scrape('laptop', 'highest_price', 3)
print(flipkart_data)
