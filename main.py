import turtle 
import random

cursor = turtle.Turtle()
screen = turtle.Screen()
text = turtle.Turtle() 
def init():
    # cursor.speed(100)
    cursor.penup()
    cursor.forward(-320)
    cursor.pendown()
    cursor.pencolor("white")
    screen.bgcolor("#13151a")
    text.color('white')
    text.setpos(0,200)
    screen.title("Turtle")
def main():
    curpos = { "x":-320,"y":0}
    total = 0
    for i in range(80):
        rand = random.randint(-100,100)
        curpos["x"] += 8
        curpos["y"] += rand
        total += rand
        
        if i % 2 == 0:
            text.clear()
            text.write(str(total)+" dollar", move=False, align="left", font=("Arial", 18, "normal")) 
        if i == 0:
            if 0 > rand:
                cursor.pencolor("red")
                cursor.write(str(rand), move=False, align="left", font=("Arial", 8, "normal")) 
            else:
                cursor.pencolor("green")
                cursor.write(str(rand), move=False, align="left", font=("Arial", 8, "normal")) 
        
        cursor.goto(curpos["x"],curpos["y"] / 1.5)
        if 0 > rand:
            cursor.pencolor("red")
            cursor.write(str(rand), move=False, align="left", font=("Arial", 8, "normal")) 
        else:
            cursor.pencolor("green")
            cursor.write(str(rand), move=False, align="left", font=("Arial", 8, "normal")) 
        prev = rand
        # print(rand)

    # 1.
    # for i in range(1400):
    #     cursor.forward(i / 10)
    #     cursor.right(1)
    #     cursor.degrees((i / 10) + 3.1416)

    # 2.
    # for i in range(1400):
    #     cursor.forward(1 + i / 3.1416)
    #     cursor.right(1 + i / 3.1416)
def end():
    turtle.done()


init()
main()
end()

