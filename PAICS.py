import re

def detect_phishing(url):
    # Regular expression to match common phishing patterns in URLs
    phishing_patterns = [
        'https?://(?:www\.)?([a-zA-Z0-9-]+\.)*([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(?:/|$)',
        'https?://(?:www\.)?(?:[a-zA-Z0-9]+\.)+(?:com|org|net|edu|gov|mil|biz|info|mobi|name|aero|asia|jobs|museum)(?:/|$)',
        'https?://(?:www\.)?(?:[a-zA-Z0-9]+\.)+(?:[a-zA-Z]{2,})(?:/|$)'
    ]

    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True
    return False

# Example usage:
url1 = "http://secure.example.com/login.html"
url2 = "http://example.com.phishing-site.com"
url3 = "http://example.com"
url4 = "https://example.com"
url5 = "https://paypal.com.example.com"

print("URL 1 (Secure):", detect_phishing(url1))
print("URL 2 (Phishing):", detect_phishing(url2))
print("URL 3 (Normal):", detect_phishing(url3))
print("URL 4 (Normal):", detect_phishing(url4))
print("URL 5 (Phishing):", detect_phishing(url5))
