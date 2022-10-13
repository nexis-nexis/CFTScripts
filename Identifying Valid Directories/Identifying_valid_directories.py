import requests
 
url = 'http://10.10.10.94'  #CHANGE THIS URL
 
f = open('/home/test/Downloads/wordlist2.txt','r').  # CHANGE PATH TO WORDLIST
 
wordlist = list(f.read().split('\n'))
 
for i in wordlist:
new_url = url + '/{}.html'.format(i)
r = requests.get(new_url)
if r.status_code!=404:
print(new_url)
 
f.close()
