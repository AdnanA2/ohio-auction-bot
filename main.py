from scrapers.bidfta_scraper import BidFTAScraper
from notifier.email_notifier import send_email_alert


def main():
    # Initialize the scraper
    scraper = BidFTAScraper()
    
    # Define keywords to search for
    keywords = ["laptop", "tv", "monitor", "tool", "pallet"]
    
    print("Searching BidFTA for items containing keywords:", keywords)
    print("=" * 50)
    
    # Get matching listings
    matching_items = scraper.get_listings(keywords)
    
    # Send email if results are not empty
    if matching_items:
        try:
            send_email_alert(matching_items)
            print(f"✅ Sent {len(matching_items)} results via email")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            print(f"Found {len(matching_items)} matching items (email failed):")
            for item in matching_items:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print("-" * 30)
    else:
        print("No matching items found.")


if __name__ == "__main__":
    main() 