from pyzbar import pyzbar
import argparse
import cv2

#Contruct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument('--i', '--image', required=True, help="Path to input image")
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["i"])

#find the barcode in the image and decode them all
barcodes = pyzbar.decode(image)

#loop over the detected barcodes
for barcode in barcodes:
    #extract the bounding box location of the barcode and
    #draw the bounding box surrounding the barcode on the image
    (x, y, w, h) = barcode.rect
    cv2.rectangle((image), (x, y), (x+w, y+h), (0, 0, 255), 2)

    #the barcode data is bytes objects so if we want to draw it so
    #our output image we have to convert it into the string first.
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    
    #draw the barcode data and barcode type on the image
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)

    #print the barcode type and data to the terminal
    print("[INFO] FOUND {} BARCODE: {}".format(barcodeType, barcodeData))

#show the output image
cv2.imshow("image", image)
cv2.waitKey(0)


