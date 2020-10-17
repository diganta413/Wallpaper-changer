import urllib.request
from PIL import Image
import requests as rq
import ctypes
import time
import os
from resizeimage import resizeimage as rs
exe = 'pic.jpg'
path = os.path.abspath(exe)
while(True):
    r = rq.get('https://api.unsplash.com/photos/random/?client_id=_eAZN8flzLkPWMNfp4Z8lWojGcypudf0OM1JCPX7QRk')
    r1 = r.json()
    s = r1['urls']['full']
    file_name = "pic.jpg"
    urllib.request.urlretrieve(s, file_name)
    im = Image.open(path)
    cover = rs.resize_cover(im, [1920, 1080])
    cover.save('pic.jpg', im.format)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    time.sleep(180)

