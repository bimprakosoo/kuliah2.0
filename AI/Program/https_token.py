from urllib.parse import urlparse
parsed = urlparse('http://blossomzones.com/')

if "https" in parsed.netloc :
    print("Website Phishing")
else:
    print("Website Legitimate")
print (parsed)