import cv2

# OPENCV:  BLUE GREEN RED
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 0, 255)


# def decryptImage(picture, output1, output2):
#     xsz, ysz = picture.shape[:2]

#     img1 = np.zeros((xsz, ysz, 3), np.uint8)
#     img2 = np.zeros((xsz, ysz, 3), np.uint8)

#     for i in range(xsz):
#         for j in range(ysz):
#             for l in range(3):
#                 v1 = format(picture[i][j][l], "08b")
#                 v2 = v1[:4] + chr(random.randint(0, 1) + 48) * 4
#                 v3 = v1[4:] + chr(random.randint(0, 1) + 48) * 4

#                 img1[i][j][l] = int(v2, 2)
#                 img2[i][j][l] = int(v3, 2)

#     cv2.imwrite(output1, img1)
#     cv2.imwrite(output2, img2)


# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x


# def readingText(picture):
#     pattern = gcd(len(picture), len(picture[0]))
#     message = ""
#     for i in range(len(picture)):
#         for j in range(len(picture[0])):
#             if (i - 1 * j - 1) % pattern == 0:
#                 if picture[i - 1][j - 1][0] != 0:
#                     message = message + chr(picture[i - 1][j - 1][0])
#     return message

# load_dotenv()
# ORIGINAL_PIC = os.getenv("ORIGINAL_PIC")
# STEGANOGRAPHY_PIC1 = os.getenv("STEGANOGRAPHY_PIC1")
# STEGANOGRAPHY_PIC2 = os.getenv("STEGANOGRAPHY_PIC2")

# ic(app.readingText(cv2.imread(ORIGINAL_PIC, 1), STEGANOGRAPHY_PIC1))


def readingText(picture, output):
    xsz, ysz = picture.shape[:2]
    temp = picture
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r) = temp[x, y]
            if g < 50 and b < 50 and r < 50:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE
    cv2.imwrite(output, temp)
    # return picture
