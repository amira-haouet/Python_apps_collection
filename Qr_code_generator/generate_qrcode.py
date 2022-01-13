import qrcode

#input_URL = "https://www.google.com/"

# just chagne this url to customise your Qr Code
input_URL1 = "https://github.com/amira-haouet"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

#qr.add_data(input_URL)
#qr.make(fit=True)

qr.add_data(input_URL1)
qr.make(fit=True)

# to create image use make image
img = qr.make_image(fill_color="black", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)
