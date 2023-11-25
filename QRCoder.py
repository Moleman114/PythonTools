'''
 Codename:     QRCoder
 Version       1.0
 Date:         2023-11-18
 Author:       Jett Bolen (Moleman114)
 Purpose:      To generate simple qr codes with text data
 Status:       Working

 External Libraries used:
 qrcode - https://github.com/lincolnloop/python-qrcode
 
 Note for future me: Colours don't seem to be working with this version of the qrcode library, update if this ever gets fixed
'''

import qrcode 
import sys

# Method to generate QR code. Most settings are hard-coded
def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="black") 
    img.save(file_name)

if not(len(sys.argv) > 1):
    text = input("Enter the data to encode: ")
    file_name = input("Enter the path to save the QR code to (the file type will be png): ") + "/qr_code.png"
else:
    if not(len(sys.argv) == 3):
        print("QRCoder Requires 2 arguments: [data] and [filepath]")
        sys.exit(-1)
    else:
        text = sys.argv[1]
        file_name = sys.argv[2] + "/qr_code.png"

# Generate the QR code
generate_qr_code(text, file_name)
print(f"QR Code saved as {file_name}")