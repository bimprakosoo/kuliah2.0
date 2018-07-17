from sklearn.naive_bayes import GaussianNB
from datetime import datetime, date
import whois

gnb = GaussianNB()
data = [
    [-1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1],
    [1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 0, 1],
    [1, 0, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1],
    [1, 0, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1],
    [1, 0, 1, 1, -1, 1, 1, 1, 1, -1, -1, 0, 1],
    [-1, 0, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1],
    [1, 0, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1],
    [1, 0, 1, 1, -1, -1, 1, -1, 1, -1, -1, 0, 1],
    [1, 0, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 0, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1],
    [-1, 1, 1, -1, -1, 0, 1, -1, 1, 1, -1, -1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1],
    [1, -1, -1, 1, -1, 0, 1, 1, 1, 1, -1, -1, 1],
    [1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 0, 1],
    [1, -1, 1, 1, -1, 0, -1, 1, -1, -1, 1, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 0, 1],
]
target = [-1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1]

# legitimate
new = [[1, 0, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1]]
#phishing
new2 = [[1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 0, 1]]

# pred = gnb.fit(data, target).predict(new2)
# if pred[0] == -1:
#     print('indentified as phising site')
# else:
#     print('indentified as secure site')

# menambah data prediksi kedalam data induk
# if (new[0] in data) == False:
#     data.append(new[0])
#     target.append(pred[0])

sample_url = "www.youtube.com"
# w = whois.whois(sample_url)
# print(len(w.creation_date))
#
# if len(w.creation_date) > 1:
#     r_date = w.creation_date[0]
# else:
#     r_date = w.creation_date
#
# date = r_date.strftime('%Y-%m-%d')
# date.split(" ")

# reg_date = datetime.strptime(date, "%Y-%m-%d")
# reg_date = datetime.strptime("1997-01-28", "%Y-%m-%d")

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(reg_date)
if age > 1:
    domain_age = 1
else:
    domain_age = -1

print("domain age : ", domain_age)
