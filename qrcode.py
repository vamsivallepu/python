import pyqrcode
url = pyqrcode.create("www.instagram.com")
url.png('uca-url.png',scale=10)
print(url.terminal(quiet_zone=1))