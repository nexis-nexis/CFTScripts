import requests
 
url = 'http://10.10.10.49'. # CHANGE THIS URL
 
f = open('/home/test/Downloads/wordlist.txt','r')  # CHANGE PATH TO WORDLIST
 
wordlist = list(f.read().split('\n'))
 
for i in wordlist:
new_url = url + '/{}.html'.format(i)
print(new_url)
 
f.close()
