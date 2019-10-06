import time
from datetime import datetime as dt

host_temp = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites = ['www.facebook.com', 'www.instagram.com',
            'www.apple.com', "www.apple.com/in"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print('working hour')
        with open(host_temp, 'r+') as files: #* here we open the _hosts_ file  
            content = files.read()           #* create var _content_ that will read the entire _hosts_ file
            for website in websites:         
                if website in content:       #* if iterables are present inside content(which is basically the hosts file)
                    pass                     #* just pass the conditonal to else
                else:
                    files.write(redirect+"   "+website+ '\n' )
    else:
        with open(host_temp,'r+') as files:
            content =files.readlines()
            files.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    files.write(line)
                files.truncate()
        print('fun hours...')
    time.sleep(3)
