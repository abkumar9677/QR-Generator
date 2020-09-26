import pyqrcode
import png

QRstring="Abhishek Kumar"
url = pyqrcode.create(QRstring)
url.png('qr.png', scale = 8)