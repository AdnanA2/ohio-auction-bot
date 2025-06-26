from playwright.sync_api import sync_playwright


class BidFTAScraper:
    def __init__(self):
        self.base_url = "https://www.bidfta.com/"
    
    def get_listings(self, keywords):
        """
        Scrape BidFTA for auction items matching the provided keywords.
        
        Args:
            keywords (list): List of keywords to search for in item titles
            
        Returns:
            list: List of dictionaries with 'title' and 'link' keys
        """
        matching_items = []
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Load the BidFTA homepage
            page.goto(self.base_url)
            
            # Wait for product cards to load
            page.wait_for_selector("div.product-thumb")
            
            # Get all product cards
            product_cards = page.query_selector_all("div.product-thumb")
            
            for card in product_cards:
                # Extract title and link from h4 a element
                title_element = card.query_selector("h4 a")
                if title_element:
                    title = title_element.inner_text().strip()
                    link = title_element.get_attribute("href")
                    
                    # Check if any keyword matches the title (case insensitive)
                    for keyword in keywords:
                        if keyword.lower() in title.lower():
                            matching_items.append({
                                "title": title,
                                "link": link
                            })
                            break  # Only add once per item even if multiple keywords match
            
            browser.close()
        
        return matching_items 