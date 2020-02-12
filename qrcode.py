#python code to create a qrcode

import pyqrcode #imports pyqrcode module into the code

url = pyqrcode.create("www.instagram.com") #creating we code and assaigning a website to our qr code

url.svg('uca-url.svg',scale=10) #creates output file(qrcode) as a .svg file

print(url.terminal(quiet_zone=1)) #rendering qrcode to terminal (able to be scanned by scanners
