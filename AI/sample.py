from sklearn.naive_bayes import GaussianNB
from datetime import datetime, date
from urllib.parse import urlencode, urlparse
from bs4 import BeautifulSoup
import whois
import re
import socket
import sys
import requests

gnb = GaussianNB()
data = []
target = []
new3 = []
temp = []

import csv
# load csv data
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    for i in lines:
        data.append([int(i[x]) for x in range(len(i)-1)])
        target.append(int(i[len(i)-1]))

def countGnb(newData):
    secure = 0
    phishing = 0
    # get total class
    indexes = []
    sc = []
    ph = []
    for i in range(len(target)):
        if target[i] == 1:
            sc.append(i)
            secure+=1
        else:
            ph.append(i)
            phishing+=1

    indexes.append(sc)
    indexes.append(ph)

    # get features
    features = []
    for x in range(len(data[0])):
        temp = []
        for row in data:
            if (row[x] in temp) == False:
                temp.append(row[x])

        temp.sort()
        features.append(temp)

    # get score for each feature
    scScore = []
    phScore = []
    ind = 0;
    for i in features:
        temp = []
        temp2 = []
        for j in i:
            total = 0
            total2 = 0
            for x in sc:
                # print("if data[",x,"][",ind,"]==",j," then append it")
                if data[x][ind] == j:
                    total += 1

            for y in ph:
                if data[y][ind] == j:
                    total2 += 1

            temp.append(total)
            temp2.append(total2)

        scScore.append(temp)
        phScore.append(temp2)
        ind+=1
    print("Total Secure site :", secure, "/", len(data))
    print("Total Phishing site :", phishing, "/", len(data))
    # print(indexes)
    # print(features)
    # print(scScore)
    # print(phScore)
    pyes = []
    pno = []
    for i in range(len(newData[0])):
        ind = features[i].index(newData[0][i])
        pyes.append(scScore[i][ind])
        pno.append(phScore[i][ind])

    print(pyes)
    print(pno)

    total_yes = 1 * (secure / len(data));
    total_no = 1 * (phishing / len(data));

    for i in pyes:
        total_yes *= (i/secure)

    for i in pno:
        total_no *= (i/phishing)

    print(total_yes)
    print(total_no)
    print("Predicted by manual gnb : ")
    if total_no > total_yes:
        print('indentified as phising site')
    else:
        print('indentified as secure site')

# f 1
def ipaddress():
    check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",parsed.netloc)
    if check:
        temp.append(-1)
    else:
        temp.append(1)

# f 2
def urllength():
    if (len(sample_url)) < 54:
        temp.append(1)
    elif (len(sample_url)) >= 54 and (len(sample_url)) <= 75:
        temp.append(0)
    else:
        if "google" in sample_url or "duckduckgo" in sample_url:
            temp.append(1)
        else:
            temp.append(-1)

# f 3
def symbol():
    if '@' in parsed.netloc:
        temp.append(-1)
    else:
        temp.append(1)

# f 4
def redirect():
    if '//' in parsed.path:
        temp.append(-1)
    else:
        temp.append(1)

# f 5
def prefixsufix():
    if '-' in parsed.netloc:
        temp.append(-1)
    else:
        temp.append(1)

# f 6
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

# f 7
def httpstoken():
    if "https" in parsed.netloc:
        temp.append(-1)
    else:
        temp.append(1)

# f 8
def checkWhois():
    w = whois.whois(sample_url)
    if w.domain_name == None and w.registrar == None:
        # print('abnormal') f 8
        temp.append(-1)
    else:
        temp.append(1)

        result = isinstance(w.creation_date, list)
        if result == False:
            r_date = w.creation_date
        else:
            r_date = w.creation_date[0]

        # age f 9
        date = r_date.strftime('%Y-%m-%d')
        date.split(" ")

        reg_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - reg_date.year - ((today.month, today.day) < (reg_date.month, reg_date.day))
        if age > 1:
            temp.append(1)
        else:
            temp.append(-1)

        #dns record f 10
        record = isinstance(w.name_servers, list)
        if result == False:
            temp.append(-1)
        else:
            temp.append(1)

# f 11
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

filename = 'dataset.csv'
# legitimate
new = [[1,1,1,1,1,1,-1,1,1,-1,1]]
#phishing
new2 = [[1,0,-1,-1,-1,1,-1,1,1,-1,-1]]

loadCsv(filename)
print('Loaded', len(data),'rows data')

# https://searchengineland.com/check-urls-indexed-google-using-python-259773
sample_url = input("INSERT URL  : ")
parsed = urlparse(sample_url)

ipaddress()
urllength()
symbol()
redirect()
prefixsufix()
portscan()
httpstoken()
checkWhois()
googleindex()


new3.append(temp)

countGnb(new3)
print(new3)
print("\nPredicted by scikit gnb : ")
pred = gnb.fit(data, target).predict(new3)
if pred[0] == -1:
    print('indentified as phising site')
else:
    print('indentified as secure site')
