from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        instanceWidth, instanceHeight = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xMax, self.xMin = x + instanceWidth, x - instanceWidth
        self.yMax, self.yMin = y + instanceHeight, y - instanceHeight
        point1 = Point(self.xMin, self.yMin)
        point2 = Point(self.xMax, self.yMax)
        self.rect = Rectangle(point1, point2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, pointClicked):
        # returns true if button active and p is inside
        return self.active and self.xMin <= pointClicked.getX() <= self.xMax and self.yMin <= pointClicked.getY() <= self.yMax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
    