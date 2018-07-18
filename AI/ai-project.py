from sklearn.naive_bayes import GaussianNB
from datetime import datetime, date
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlparse
import test
import socket
import sys
import requests

gnb = GaussianNB()
data = []
target = []

# legitimate
new = [[1, 0, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1]]
#phishing
new2 = [[1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 0, 1]]

new3 = []
temp = []

sample_url = input("INSERT URL  : ")
parsed = urlparse(sample_url)

def portscan():
    remoteServerIP = socket.gethostbyname(parsed.netloc)
    print("-" * 60)
    print("Please Wait, Scanning Remote Host", remoteServerIP)
    print("-" * 60)
    t1 = datetime.now()
    list = 21, 22, 23, 80, 443, 445, 1433, 1521, 3306, 3389
    port_open = [21, 80, 443, 3306, 1521]
    open_port = []
    try:
        for port in list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}  :        Open".format(port))
                open_port.append(port)
            else:
                print("Port {}  :        Close".format(port))
    except KeyboardInterrupt:
        print("You Pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1
    if open_port <= port_open:
        temp.append(1)
    else:
        temp.append(-1)
    print(open_port)
    print("Scanning Completed in : ", total)

def googleindex():
    proxies = {
        'https': 'https://localhost:8123',
        'http': 'http://localhost:8123'
    }
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    query = {'q': 'info:' + sample_url}
    google = "https://www.google.com/search?" + urlencode(query)
    data = requests.get(google, headers=headers, proxies=proxies)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    try:
        check = soup.find(id="rso").find("div").find("div").find("h3").find("a")
        href = check['href']
        # print(sample_url + " is indexed!")
        temp.append(1)
    except AttributeError:
        # print(sample_url + " is NOT indexed!")
        temp.append(-1)


def prefixsufix():
    if '-' in parsed.netloc:
        temp.append(-1)
    else:
        temp.append(1)

def httpstoken():
    if "https" in parsed.netloc:
        temp.append(-1)
    else:
        temp.append(1)

prefixsufix()
portscan()
httpstoken()
googleindex()
new3.append(temp)
print(new3)
# print(parsed)
