import requests
 
url = 'https://securityhub.site/files/Peter.zip' # CHANGE THIS URL 
r = requests.get(url, allow_redirects=True)
open('Peter.zip', 'wb').write(r.content) 
