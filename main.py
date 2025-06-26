from scrapers.bidfta_scraper import BidFTAScraper


def main():
    # Initialize the scraper
    scraper = BidFTAScraper()
    
    # Define keywords to search for
    keywords = ["laptop", "tv", "monitor", "tool", "pallet"]
    
    print("Searching BidFTA for items containing keywords:", keywords)
    print("=" * 50)
    
    # Get matching listings
    matching_items = scraper.get_listings(keywords)
    
    # Print results
    if matching_items:
        print(f"Found {len(matching_items)} matching items:")
        for item in matching_items:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print("-" * 30)
    else:
        print("No matching items found.")


if __name__ == "__main__":
    main() 