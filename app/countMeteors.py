import cv2

# OPENCV:  BLUE GREEN RED
WHITE = (255, 255, 255, 255)
RED = (0, 0, 255, 255)
BLUE = (255, 0, 0, 255)


def meteorsOnly(picture, output):
    xsz, ysz = picture.shape[:2]
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = picture[x, y]
            if (b, g, r, _) != RED and (b, g, r, _) != BLUE:
                picture[x, y] = WHITE
    cv2.imwrite(output, picture)
    return picture


def countMeteorsAndWaterMeteors(picture, output):
    picture = meteorsOnly(picture, output)
    count = overWater = loopCount = 0
    isOverWater = False
    xsz, ysz = picture.shape[:2]
    for y in range(ysz):
        loopCount = 0
        isOverWater = False
        for x in range(xsz):
            (b, g, r, _) = picture[x, y]
            if g == 255:
                continue
            elif r == 255:
                loopCount += 1
            elif b == 255:
                isOverWater = True
        count += loopCount
        if isOverWater:
            overWater += loopCount

    return count, overWater
