#for this first install pip install "qrcode[pil]"
import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4)
qr.add_data("https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("qrcode.png")