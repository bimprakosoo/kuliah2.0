from urllib.parse import urlparse
parsed = urlparse('https://123.123.123.123/hallo.html')

if "https" in parsed.netloc :
    print("Website Phishing")
else:
    print("Website Legitimate")
print (parsed)