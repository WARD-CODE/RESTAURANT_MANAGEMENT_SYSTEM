import cv2
from pyzbar.pyzbar import decode


def get_barcode(image_file):
    img = cv2.imread(image_file)
    barcodes = decode(img)
    if barcodes:
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            print(f"Barcode Type: {barcode_type}, Data: {barcode_data}")
        else:
            print("No barcode found in the image.")
    return barcode_data