sample_url = input("INSERT URL  : ")

if (len(sample_url)) < 54:
    print("Website Legimite")
elif (len(sample_url)) >= 54 and (len(sample_url)) <= 75:
    print("Suspicious")
else:
    if "google" in sample_url or "duckduckgo" in sample_url:
        print("Legitimate")
    else:
        print("Phishing")