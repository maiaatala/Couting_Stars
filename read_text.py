import cv2
import pytesseract
from icecream import ic

dotsOnlyPic = "./meteor_challenge_01/dotsOnWhite.png"


def ocrCore(pic):
    text = pytesseract.image_to_string(pic)
    return text


pic = cv2.imread(dotsOnlyPic)


ic(ocrCore(pic))
