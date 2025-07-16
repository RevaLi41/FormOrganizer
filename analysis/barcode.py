import cv2
from pyzbar.pyzbar import decode



if __name__ == '__main__':
    img = cv2.imread('../training-data/ID Back/IMG_3392.JPG')
    print(decode(img))