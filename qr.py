import qrcode

# Menü URL'si (HTML menünüzün bulunduğu adres)
menu_url = "file:///C:/Users/hasnk/OneDrive/Masaüstü/ozzys%20qr/menu.html"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(menu_url)
qr.make(fit=True)

# QR kodu görseli oluşturma
img = qr.make_image(fill='black', back_color='white')

# Görseli kaydetme
img.save("menu_qrcode.png")
