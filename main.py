from PIL import Image
from icecream import ic

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)


def findColor(picture, color="white"):
    if color == "white":
        max_val = 0
        for (r, g, b, _) in picture.getdata():
            if r + g + b > max_val:
                max_val = r + g + b
        return max_val
    if color == "red":
        maxR = 0
        lowB = lowG = 255
        for (r, g, b, _) in picture.getdata():
            if r > maxR and b + g < lowB + lowG:
                maxR, lowB, lowG = r, g, b
        return maxR, lowB, lowG


def findColorAndCoords(picture, color="white"):
    xsz, ysz = picture.size
    temp = picture.load()
    if color == "white":
        bx = by = max_val = 0
        for x in range(xsz):
            for y in range(ysz):
                r, g, b, _ = temp[x, y]
                if r + b + g > max_val:
                    bx, by, max_val = x, y, r + g + b
        return (bx, by), max_val


def starsOnly(picture, treshold):
    treshold -= 100
    xsz, ysz = picture.size
    temp = picture.load()
    for x in range(xsz):
        for y in range(ysz):
            (r, g, b, _) = temp[x, y]
            if r + g + b >= treshold:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE


def meteorsOnly(picture, thr, thb, thg):
    thr, thb, thg = thr - 50, thb + 50, thg + 50
    xsz, ysz = picture.size
    temp = picture.load()
    for x in range(xsz):
        for y in range(ysz):
            (r, g, b, _) = temp[x, y]
            if r >= thr and g <= thg and b <= thb:
                temp[x, y] = RED
            else:
                temp[x, y] = WHITE


def dotsOnly(picture):
    xsz, ysz = picture.size
    temp = picture.load()
    for x in range(xsz):
        for y in range(ysz):
            (r, g, b, _) = temp[x, y]
            if r >= 200:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE


def fillNeighbors(pic, xsz, ysz, x, y):
    if pic[x, y] == WHITE:
        return
    pic[x, y] = WHITE
    if x > 0:
        fillNeighbors(pic, xsz, ysz, x - 1, y)
    if x < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x + 1, y)
    if y > 0:
        fillNeighbors(pic, xsz, ysz, x, y - 1)
    if x < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x, y + 1)


def countStars(picture):
    count = 0
    temp = picture.load()
    xsz, ysz = picture.size
    for y in range(ysz):
        for x in range(xsz):
            if temp[x, y] == BLACK:
                count += 1
                fillNeighbors(temp, xsz, ysz, x, y)
    return count


def countMeteors(picture):
    count = 0
    temp = picture.load()
    xsz, ysz = picture.size
    for y in range(ysz):
        for x in range(xsz):
            if temp[x, y] == RED:
                count += 1
                fillNeighbors(temp, xsz, ysz, x, y)
    return count


originalPic = "./meteor_challenge_01/meteor_challenge_01.png"
starsOnlyPic = "./meteor_challenge_01/blackStarsOnWhite.png"
meteorsOnlyPic = "./meteor_challenge_01/redMeteorsOnWhite.png"
dotsOnlyPic = "./meteor_challenge_01/dotsOnWhite.png"
testStars = "./meteor_challenge_01/testStarsCount.png"
testMeteor = "./meteor_challenge_01/testStarsMeteor.png"

pic = Image.open(originalPic)

# pic = Image.open(originalPic)
# max_white = findColor(pic)
# starsOnly(pic, max_white)
# pic.save(starsOnlyPic)

# pic = Image.open(originalPic)
# redR, redB, redG = findColor(pic, color="red")
# meteorsOnly(pic, redR, redB, redG)
# pic.save(meteorsOnlyPic)

dotsOnly(pic)
pic.save(dotsOnlyPic)


pic = Image.open(starsOnlyPic)
ic(countStars(pic))
pic.save(testStars)

pic = Image.open(meteorsOnlyPic)
ic(countMeteors(pic))
pic.save(testMeteor)
