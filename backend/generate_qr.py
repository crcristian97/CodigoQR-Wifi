from wifi_qrcode_generator import wifi_qrcode

def generate_qr(ssid, password):
    try:
        qr_code = wifi_qrcode(ssid, hidden=False, authentication_type="WPA", password=password)
        image_path = "static/wifi_qr_code.png"
        qr_code_img = qr_code.make_image()
        qr_code_img.save(image_path)
        return image_path
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None
