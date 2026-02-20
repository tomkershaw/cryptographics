import turtle
t = turtle.Turtle()
turtle.tracer(0)
x = 0
y = 0
w = 50
h = w
r = h/2



def draw_clock(t, x, y, w, h):
    t.fillcolor("#D0D0D0")
    t.begin_fill()
    t.teleport(x+w/2, y-h*3/4)
    t.circle(h/4)
    t.end_fill()
    t.teleport(x+w/2, y-h/2)
    t.seth(150)
    t.fd(h/6)
    t.bk(h/6)
    t.seth(30)
    t.fd(h/6)
    t.seth(0)
    t.fillcolor("black")
    t.teleport(x+w/2, y)

def draw_key(t:turtle.Turtle, x:float, y:float, w:float, h:float):
    t.fillcolor("#D0D0D0")
    t.begin_fill()
    t.teleport(x+w/2, y-h*3/4)
    t.circle(h/4, 275)
    t.seth(225)
    t.fd(h/2)
    t.lt(45)
    t.fd(h/4)
    t.lt(90)
    t.fd(h/4)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.lt(90)
    t.fd(h/8)
    t.rt(90)
    t.fd(h/8)
    t.end_fill()
    t.teleport(x+w/2, y-h/2)
    t.fillcolor("black")
    t.teleport(x+w/2, y)
    t.seth(0)

def draw(t=None, element="agent", ornament="", text="", x=0, y=0, w=100, h=100):
    if not t:
        t=turtle.Turtle()
    
    if element == "connection":
        t.forward(w)
        if ornament == "arrow":
            t.stamp()
    elif element == "agent":
        r=w/2
        t.teleport(x, y-r)
        t.circle(r)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+r, y)
    elif element == "message":
        t.teleport(x-w/2, y+h/2)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.teleport(x, y-8)
        t.write(text, align="center", font = ("Arial", 8, "bold"))
        t.teleport(x+w/2, y)

    if ornament == "clock":
        draw_clock(t, x, y, w, h)
    elif ornament == "key":
        draw_key(t, x, y, w, h)

def process(protocol:str, x=0, y=0, w=50, h=50):
    els = protocol.split()
    for el in els:
        eltype = el[0]
        if len(el) > 1:
            elorn = el[1]
        else:
            elorn = ""
        match eltype:
            case eltype if eltype in "ABCDE" and elorn == "k":
                print("agent", eltype)
                draw(t, element='agent', ornament="key", text=eltype, x=x+w/2, y=y, w=w, h=h)
            case eltype if eltype in "ABCDE":
                print("agent", eltype)
                draw(t, element='agent', text=eltype, x=x+w/2, y=y, w=w, h=h)
            case "-" if elorn == ">":
                print("arrow")
                draw(t, element='connection', ornament="arrow", w=w)
            case "-":
                print("line")
                draw(t, element='connection', w=w)
            case "#" if elorn == "n":
                print("nonce")
                draw(t, element='message', ornament="clock", text="a", x=x+w/2, y=y, w=w, h=h)
            case "#" :
                print("message")
                draw(t, element='message', text="a", x=x+w/2, y=y, w=w, h=h)
            case _:
                print("?")
        x += w
    return {"els":els, "x":x, "y":y}
        
assert process("A -> B")["els"] == ["A", "->", "B"]
assert process("Ak - #n -> B", y=100)["els"] == ["Ak", "-", "#n", "->", "B"]

t.hideturtle()
turtle.update()
turtle.done()