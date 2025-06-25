import qrcode
from PIL import Image

name = input("Enter the first name: ")
title = input("Enter the last name: ")
phone = input("Enter the phone number: ")
email = input("Enter the email: ")

vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name} {title}
TEL;TYPE=CELL:+91-{phone}
EMAIL:{email}
END:VCARD
"""

color = input("Enter the QR inner color: ")
back_color = input("Enter the QR background color: ")

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

img = qr.make_image(fill_color=color, back_color=back_color).convert("RGB")

img.save("vcard_qr.png")
img.save("vcard_qr.jpg")
