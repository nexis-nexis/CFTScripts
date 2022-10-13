
import hashlib
 
#input hash to be cracked
 
hash = 'cd13b6a6af66fb774faa589a9d18f906' # SUPPLY HASH VALUE
#input the wordlists
f = open('/home/test/Downloads/wordlist2.txt', 'r') 
 
wordlist = list(f.read().split('\n'))
 
# let's compare the md5 hash with each word in the list. if there is a coresponding hash then we got a hash
 
for i in wordlist:
temporaryhash = hashlib.md5(i.encode())
# use the encode function to encode the string
# this is the fianl hexdecimal hash for  the wordlist
hexhash = temporaryhash.hexdigest()
if hexhash == hash:
print (i)
# break indicate that we have found the hash and we can successfully end the loop
break
 
 
 
f.close()
