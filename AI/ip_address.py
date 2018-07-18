import re
from urllib.parse import urlparse
# parsed = urlparse('http://https-www-paypal-it-webapps-mpp-home.soft-hair.com')
parsed = urlparse('http://12.23.123.23/crot/didalam')
# Precompile the patterns
# regexes = [
#     re.compile(p)
#     for p in ['this', 'that']
# ]
# text = 'Does that text match the pattern?'
#
# print('Text: {!r}\n'.format(text))
#
# for regex in regexes:
#     print('Seeking "{}" ->'.format(regex.pattern),
#           end=' ')
#
#     if regex.search(text):
#         print('match!')
#     else:
#         print('no match')

ohh = '123.123.123.123'
crot = 'didalam'
hmm = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",parsed.netloc)
if hmm:
    print("ahhh bang ahhh ahhh i'm phishing")
else:
    print('cupu lu neng')
# if hmm == 'none':
#     print('lagi bang')
# else:
#     print('udahan yaa neng')