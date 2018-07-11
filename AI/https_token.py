from urllib.parse import urlparse
parsed = urlparse('http://https-www-paypal-it-webapps-mpp-home.soft-hair.com')

if "https" in parsed.netloc :
    print("Website Phishing")
else:
    print("Website Legitimate")
print (parsed)