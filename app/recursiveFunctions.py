WHITE = (255, 255, 255, 255)


def fillNeighbors(pic, xsz, ysz, x, y):
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return
    pic[x, y] = WHITE
    if x > 0:
        fillNeighbors(pic, xsz, ysz, x - 1, y)
    if x < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x + 1, y)
    if y > 0:
        fillNeighbors(pic, xsz, ysz, x, y - 1)
    if y < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x, y + 1)


def xLen(pic, xsz, x, y):
    if x >= xsz:
        return 0
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return 0
    return 1 + xLen(pic, xsz, (x + 1), y)


def yLen(pic, ysz, x, y):
    if y >= ysz:
        return 0
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return 0
    return 1 + yLen(pic, ysz, x, y + 1)
