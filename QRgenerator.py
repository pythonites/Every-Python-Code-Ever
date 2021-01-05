import pyqrcode 
import png 
from pyqrcode import QRCode 

s = input("Enter string to make it QR: ")

url = pyqrcode.create(s) 
url.png('/storage/emulated/0/myqr.png', scale = 10)
