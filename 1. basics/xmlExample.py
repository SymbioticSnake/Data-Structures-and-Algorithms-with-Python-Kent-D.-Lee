class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
    
    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return '<Command x="’ + str(self.x) + ’" y="’ + str(self.y) + ’" width="’ +  \
            str(self.width) + ’" color="’ + self.color + ’">GoTo</Command>'

import xml.dom.minidom

