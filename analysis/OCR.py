from PIL import Image

import pytesseract



if __name__ == '__main__':


    img_path = '../training-data/ID Front/IMG_3391.JPG'
    img = Image.open(img_path).convert('RGB')  # This forces it into a supported mode

    print(pytesseract.image_to_string(img))

    # print(pytesseract.image_to_string(Image.open('../training-data/ID Front/IMG_3391.JPG')))
    # print(pytesseract.image_to_string(Image.open('test.jpg')))