import cv2
import cvlib as cv
import base64
import uuid
import os

images_path = "./img/"


def learn_stuff(base64_bytes):
    filename = uuid.uuid4().hex
    decodeit = open(images_path + filename, 'wb')
    decodeit.write(base64.b64decode((base64_bytes)))

    im = cv2.imread(images_path + filename)
    bbox, label, conf = cv.detect_common_objects(im)

    if os.path.exists(images_path + filename):
        os.remove(images_path + filename)

    return label.count('car'), label.count('truck'), label.count('busses')
