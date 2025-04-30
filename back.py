import qrcode

# Input from user
data = input("Enter the text or URL to generate QR Code: ")

# Create QR code object
qr = qrcode.make(data)

# Save the QR code image
qr.save("qr_code.png")

print("QR Code generated and saved as qr_code.png")
