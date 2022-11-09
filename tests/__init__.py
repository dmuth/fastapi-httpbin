

import fs
import cv2


def decode_qrcode(qrcode):

    tmp_fs = fs.open_fs('temp://')

    with tmp_fs.open("file.png", "wb") as file:
        file.write(qrcode)
        filename = file.name.decode("utf-8")

    image = cv2.imread(filename)

    #cv2.imshow('Image', image) # Debugging
    #cv2.waitKey(0) # Debugging

    detector = cv2.QRCodeDetector()
    retval, _, _  = detector.detectAndDecode(image)

    return(retval)

