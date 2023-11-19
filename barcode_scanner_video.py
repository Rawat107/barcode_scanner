from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--o", "--output", type=str, default="barcode.csv",
                help="Path to output CSV file containing barcodes")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

#open csv file to write and initialize the set of
#barcode has been found thus far
csv = open(args["o"], "w")
found = set()


#loop over the frame from video stream
while True:

    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)


#loop over detected baar code

    for barcode in barcodes:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{}, ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if barcodeData not in found:
            csv.write("{}, {}\n".format(datetime.datetime.now(), 
                                        barcodeData))
            csv.flush()
            found.add(barcodeData)    
    
    cv2.imshow("Barcode scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

print("[INFO] cleaning up.....")
csv.close()
cv2.destroyAllWindows()
vs.stop()