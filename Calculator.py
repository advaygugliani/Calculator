import turtle
display = ""

nums = ["0","1","2","3","4","5","6","7","8","9"]
def DisplayWrite(writepart):
    global pen
    pen.clear()
    pen.write("{}".format(writepart), align="right", font=("Arial", 20, "normal"))

def ZeroClick(x,y):
    global display,pen
    display += ("0")
    DisplayWrite(display)
def OneClick(x,y):
    global display,pen
    display += ("1")
    DisplayWrite(display)
def TwoClick(x,y):
    global display,pen
    display += ("2")
    DisplayWrite(display)
def ThreeClick(x,y):
    global display,pen
    display += ("3")
    DisplayWrite(display)
def FourClick(x,y):
    global display,pen
    display += ("4")
    DisplayWrite(display)
def FiveClick(x,y):
    global display,pen
    display += ("5")
    DisplayWrite(display)
def SixClick(x,y):
    global display,pen
    display += ("6")
    DisplayWrite(display)
def SevenClick(x,y):
    global display,pen
    display += ("7")
    DisplayWrite(display)
def EightClick(x,y):
    global display,pen
    display += ("8")
    DisplayWrite(display)
def NineClick(x,y):
    global display,pen
    display += ("9")
    DisplayWrite(display)
def Add(x,y):
    global display,pen
    display += ("+")
    DisplayWrite(display)
def Subtract(x,y):
    global display,pen
    display += ("-")
    DisplayWrite(display)
def Multiply(x,y):
    global display,pen
    display += ("x")
    DisplayWrite(display)
def Divide(x,y):
    global display,pen
    display += ("÷")
    DisplayWrite(display)
def Clear(x,y):
    global display,pen
    display = ""
    DisplayWrite(display)
def Answer(x,y):
    global display,pen,final_display,ans
    n = ""
    final_display = []
    for x in display:
        if x in nums:
            n += x
        else:
            final_display.extend([float(n),x])
            n = ""
    else:
        final_display.append(float(n))

    dis = []
    #DIVIDE
    t = False
    for i in range(len(final_display)):
        x = final_display[i]
        if x == "÷":
            dis.pop()
            dis.append(float(final_display[i-1])/float(final_display[i+1]))
            t = True
        else:
            if not t:
                dis.append(x)
            if t:
                t = False
    final_display = dis
    dis = []
    #Multiply
    t = False
    for i in range(len(final_display)):
        x = final_display[i]
        if x == "x":
            dis.pop()
            dis.append(float(final_display[i-1]) * float(final_display[i+1]))
            t = True
        else:
            if not t:
                dis.append(x)
            if t:
                t = False
    final_display = dis
    ans = final_display[0]
    for i in range(len(final_display)):
        if final_display[i] == "-":
            ans -= final_display[i+1]
        elif final_display[i] == "+":
            ans += final_display[i+1]
    display = str(ans)
    DisplayWrite(display)

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Calculator")
wn.setup(width=400,height=600)


wn.addshape("pics/0.gif")
wn.addshape("pics/1.gif")
wn.addshape("pics/2.gif")
wn.addshape("pics/3.gif")
wn.addshape("pics/4.gif")
wn.addshape("pics/5.gif")
wn.addshape("pics/6.gif")
wn.addshape("pics/7.gif")
wn.addshape("pics/8.gif")
wn.addshape("pics/9.gif")
wn.addshape("pics/x.gif")
wn.addshape("pics/add.gif")
wn.addshape("pics/ans.gif")
wn.addshape("pics/divide.gif")
wn.addshape("pics/-.gif")
wn.addshape("pics/c.gif")

zero = turtle.Turtle()
zero.speed(0)
zero.shape("pics/0.gif")
zero.penup()
zero.goto(-80,-210)
zero.onclick(ZeroClick)

one = turtle.Turtle()
one.speed(0)
one.shape("pics/1.gif")
one.penup()
one.goto(-160,0)
one.onclick(OneClick)

two = turtle.Turtle()
two.shape("pics/2.gif")
two.speed(0)
two.penup()
two.goto(-80,0)
two.onclick(TwoClick)

three = turtle.Turtle()
three.shape("pics/3.gif")
three.speed(0)
three.penup()
three.goto(0,0)
three.onclick(ThreeClick)

four = turtle.Turtle()
four.shape("pics/4.gif")
four.speed(0)
four.penup()
four.goto(-160,-70)
four.onclick(FourClick)

five = turtle.Turtle()
five.shape("pics/5.gif")
five.speed(0)
five.penup()
five.goto(-80,-70)
five.onclick(FiveClick)

six = turtle.Turtle()
six.shape("pics/6.gif")
six.speed(0)
six.penup()
six.goto(0,-70)
six.onclick(SixClick)

seven = turtle.Turtle()
seven.shape("pics/7.gif")
seven.speed(0)
seven.penup()
seven.goto(-160,-140)
seven.onclick(SevenClick)

eight = turtle.Turtle()
eight.shape("pics/8.gif")
eight.speed(0)
eight.penup()
eight.goto(-80,-140)
eight.onclick(EightClick)

nine = turtle.Turtle()
nine.shape("pics/9.gif")
nine.speed(0)
nine.penup()
nine.goto(0,-140)
nine.onclick(NineClick)

add = turtle.Turtle()
add.shape("pics/add.gif")
add.speed(0)
add.penup()
add.goto(80,-70)
add.onclick(Add)

subtract = turtle.Turtle()
subtract.shape("pics/-.gif")
subtract.speed(0)
subtract.penup()
subtract.goto(80,-140)
subtract.onclick(Subtract)

multiply = turtle.Turtle()
multiply.shape("pics/x.gif")
multiply.speed(0)
multiply.penup()
multiply.goto(-160,-210)
multiply.onclick(Multiply)

divide = turtle.Turtle()
divide.shape("pics/divide.gif")
divide.speed(0)
divide.penup()
divide.goto(0,-210)
divide.onclick(Divide)

ans = turtle.Turtle()
ans.shape("pics/ans.gif")
ans.speed(0)
ans.penup()
ans.goto(80,-210)
ans.onclick(Answer)

clear = turtle.Turtle()
clear.shape("pics/c.gif")
clear.speed(0)
clear.penup()
clear.goto(80,0)
clear.onclick(Clear)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(100,160)

while True:
    wn.update()