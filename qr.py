import qrcode


menu_url = "https://hasnkpl.github.io/ozzys-menu-/"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(menu_url)
qr.make(fit=True)


img = qr.make_image(fill='black', back_color='white')


img.save("menu_qrcode.png")
