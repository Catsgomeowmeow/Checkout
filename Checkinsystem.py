from __future__ import print_function
import cv2
from pyzbar import pyzbar
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
def cardreader():
    # construct the argument parser and parse the arguments
    # load the input image
    image = cv2.imread(r'M:\Documents\Projects\QR.png')

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        name = barcode.data.decode("utf-8")

        # draw the barcode data and barcode type on the image
        text = "{}".format(barcodeData)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

        if name == 'S16950636':
            print('hello Isamu')

        else:
            print('notfound')


    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    return name

def scanner():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0
    x = 1
    while x == 1:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "QR.png"
            y = cv2.imwrite(img_name, frame)

            x =2
def qrin():
    # construct the argument parser and parse the arguments
    # load the input image
    image = cv2.imread(r'M:\Documents\Projects\QR.png')

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        name = barcode.data.decode("utf-8")

        # draw the barcode data and barcode type on the image
        text = "{}".format(barcodeData)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

        # print the barcode type and data to the terminal
        print("[INFO] Found barcode: {}".format(barcodeData))

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    return name

scanner()
name = cardreader()
print(name)

