import requests
from stem import Signal
from stem.control import Controller
from config import password

def sess():
    session = requests.session()
    session.proxies = {}
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'
    return session

headers ={ 'User-Agent': "GarlicBread Search Engine Crawler" }
#usage sess.get(url , headers=headers)

def change_identity():
    with Controller.from_port(port = 9051) as c:
        c.authenticate(password=password)
        c.signal(Signal.NEWNYM)


#a = sess().get('http://httpbin.org/ip' , headers=headers)
#print(a.text)
# a tor ip
#change_identity()
#
#
#a = sess().get('http://httpbin.org/ip' , headers=headers)
#print(a.text)
#
# a new tor ip
#a = sess().get('https://httpbin.org/user-agent' , headers=headers)
#print(a.text)
#desirable UserAgent

