class Rect(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def hit_test(self, x, y):
        if x >= self.x and x < self.x + self.width:
            if y >= self.y and y < self.y  + self.height:
                return True
        return False