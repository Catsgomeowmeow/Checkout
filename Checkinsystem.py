from __future__ import print_function
import cv2
# from imutils.video import VideoStream
from pyzbar import pyzbar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
today = time.strftime("%b %d %Y")
now = datetime.datetime.now()
LARGE_FONT = ("Verdana", 12)
import tkinter as tk
from tkinter import ttk,Entry,StringVar, Tk,Label,Button,Entry,IntVar,W,END,Toplevel,LEFT,RIGHT,BOTTOM,TOP
import os
# import argparse
# import datetime
# import imutils
# import time


##########GOOGLE SHEETS SETUP ##############################################################
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\Isamu Naets\Downloads\Checkout-7aea39f71095.json', scope)
client = gspread.authorize(creds)

 # Find a workbook by name and open the first sheet
 # Make sure you use the right name here.
sheet = client.open("Laptops").sheet1
##########################################################################################################################

def cardreader2():
    # construct the argument parser and parse the arguments
    # load the input image
    image = cv2.imread('qr.png')

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

def scanner_id():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("ID Scan")

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
            img_name = "ID.png"
            y = cv2.imwrite(img_name, frame)
            x = 2

def scanner_qr():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("QR Scan")

    img_counter = 0
    x = 1
    while x == 1:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "qr.png"
            y = cv2.imwrite(img_name, frame)
            x = 2

        # scanner()
# name = cardreader()

class Mainpage(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        top = tk.Frame(self)
        bottom = tk.Frame(self)
        top.pack(side=TOP)
        bottom.pack(side=BOTTOM)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(2, weight=10)
        container.grid_columnconfigure(2, weight=10)

        self.frames = {}

        for F in (StartPage, CheckIn,  checkout):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=5, column=5, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What would you like to do ? ", font=LARGE_FONT)
        label.pack(pady=10, padx=100,)

        Cin = ttk.Button(self, text="Return a laptop",
                            command=lambda: controller.show_frame(CheckIn))
        Cin.pack(pady=1, padx=10,side=TOP)

        Cout = ttk.Button(self, text="Check-Out a laptop",
                            command=lambda: controller.show_frame(checkout))
        Cout.pack(pady=1, padx=10,side=TOP)
        closebutton = ttk.Button(self,text="Close",command = controller.destroy)
        closebutton.pack(pady=50,side=BOTTOM)
class checkout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global id, name_id
        ##############################################################################################################
        def cardreader():
            scanner_id()
            # construct the argument parser and parse the arguments
            # load the input image
            global name , name_id
            image = cv2.imread('ID.png')

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
                    name = 'Isamu Naets'

                else:
                    print('notfound')

            # show the output image
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            id = ttk.Entry(self)
            id.insert(END,name)
            id.pack()
            print(name)
            scanPC = ttk.Button(self, text="Scan Laptop")
            scanPC.configure(command=lambda: qrin2())
            scanPC.pack()
            ############################################################################################################
            def qrin2():
                scanner_qr()
                # construct the argument parser and parse the arguments
                # load the input image
                global laptop,name_id
                image = cv2.imread('qr.png')

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
                    laptop = barcode.data.decode("utf-8")

                    # draw the barcode data and barcode type on the image
                    text = "{}".format(barcodeData)
                    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)

                    # print the barcode type and data to the terminal
                    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

                    if laptop == 'S16950636':
                        print('hello Isamu')

                    else:
                        print('notfound')

                # show the output image
                cv2.imshow("Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                idl = ttk.Entry(self)
                idl.insert(END, laptop)
                idl.pack()
                name_id = id.get()
                # print("laptop is %r" %name_id)

        def apply():

            x = sheet.find(laptop)

            sheet.update_cell(x._row,3,name_id)
            print(today)
            sheet.update_cell(x._row,5,today)
            sheet.update_cell(x.row,4,'')
            os.remove("ID.png")
            os.remove("qr.png")
            controller.destroy()

        label = tk.Label(self, text="Check out a laptop", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        scanID = ttk.Button(self,text="ScanID")
        scanID.configure(command = lambda: cardreader())
        scanID.pack()




        # applybutton = ttk.Button(self,text"Apply",command= submit)
        # applybutton.pack(side=BOTTOM)
        closebutton = ttk.Button(self,text="Close",command = controller.destroy)
        closebutton.pack(side = BOTTOM)


        button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=BOTTOM)
        apply = ttk.Button(self,text="Apply" ,command = apply)
        apply.pack(side=  BOTTOM)

class CheckIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global id ,name_idin
        ##############################################################################################################
        def cardreader():
            scanner_id()
            # construct the argument parser and parse the arguments
            # load the input image
            global name ,name_idin
            image = cv2.imread('ID.png')

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
                    name = 'Isamu Naets'

                else:
                    print('notfound')

            # show the output image
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            id = ttk.Entry(self)
            id.insert(END,name)
            id.pack()
            print(name)
            scanPC = ttk.Button(self, text="Scan Laptop")
            scanPC.configure(command=lambda: qrin2())
            scanPC.pack()
            ############################################################################################################
            def qrin2():
                scanner_qr()
                # construct the argument parser and parse the arguments
                # load the input image
                global laptop ,name_idin
                image = cv2.imread('qr.png')

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
                    laptop = barcode.data.decode("utf-8")

                    # draw the barcode data and barcode type on the image
                    text = "{}".format(barcodeData)
                    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)

                    # print the barcode type and data to the terminal
                    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

                    if laptop == 'S16950636':
                        print('hello Isamu')

                    else:
                        print('notfound')

                # show the output image
                cv2.imshow("Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                idl = ttk.Entry(self)
                idl.insert(END, laptop)
                idl.pack()
                name_idin = id.get()

        def apply():
            x = sheet.find(laptop)
            sheet.update_cell(x._row,3,name_idin +'(returned)')
            print(today)
            sheet.update_cell(x._row,4,today)
            os.remove("ID.png")
            os.remove("qr.png")
            controller.destroy()

        label = tk.Label(self, text="Return a laptop", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        scanID = ttk.Button(self,text="ScanID")
        scanID.configure(command = lambda: cardreader())
        scanID.pack()




        # applybutton = ttk.Button(self,text"Apply",command= submit)
        # applybutton.pack(side=BOTTOM)
        closebutton = ttk.Button(self,text="Close",command = controller.destroy)
        closebutton.pack(side = BOTTOM)


        button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=BOTTOM)

        apply = ttk.Button(self,text="Apply" ,command = apply)
        apply.pack(side=  BOTTOM)



app = Mainpage()
app.mainloop()
