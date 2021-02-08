import turtle

def main():
    filename = input("Please enter drawing filename: ")    
    
    t = turtle.Turtle()
    screen = t.getscreen()

    file = open(filename, "r")

    if filename == "moduleExample.txt":

        for line in file:
            text = line.strip()
            commandList = text.split(",")
            command = commandList[0]

            if command == "goto":
                x = float(commandList[1])
                y = float(commandList[2])
                width = float(commandList[3])
                color = commandList[4].strip()
                t.width(width)
                t.pencolor(color)
                t.goto(x, y)
            
            elif command == "circle":
                radius = float(commandList[1])
                width = float(commandList[2])
                color = commandList[3].strip()
                t.width(width)
                t.pencolor(color)
                t.circle(radius)

            elif command == "beginfill":
                color = commandList[1].strip()
                t.fillcolor(color)
                t.begin_fill()

            elif command == "endfill": t.end_fill()
            elif command == "penup": t.penup()
            elif command == "pendown": t.pendown()
            else: print("Unknown command found in file:", command)

    elif filename == "moduleExample2.txt":
        
        command = file.readline().strip()
        while command != "":

            if command == "goto":
                x = float(file.readline())
                y = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.goto(x,y)

            elif command == "circle":
                radius = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.circle(radius)
            
            elif command == "beginfill":
                color = file.readline().strip()
                t.fillcolor(color)
                t.begin_fill()
            
            elif command == "endfill": t.end_fill()
            elif command == "penup": t.penup()
            elif command == "pendown": t.pendown()
            else: print("Unknown command found in file:", command)

            command = file.readline().strip()
        
    file.close()
    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()