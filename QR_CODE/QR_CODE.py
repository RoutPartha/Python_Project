##first go to Terminal and install type(pip install pyqrcode)
##Then install (pip install pypng) 

import pyqrcode 
name='https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit'
p=pyqrcode. create(name)
p.png('test.png',scale=10)


import os
os.system('test.png') ##it open our QR_CODE


##Run it in (Run Python File in Terminal)