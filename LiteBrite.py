#source code from TokyoEdTech(youtube)
import turtle
WIDTH = 820
HEIGHT = 140
win = turtle.Screen()
win.title("Lite-Brite")
win.bgcolor("Black")
win.setup(WIDTH, HEIGHT)
color_codes = {"r":"red","o":"orange","y":"yellow","g":"green","b":"blue","w":"white","p":"pink"," ":"black"}
pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.shape("circle")
def draw_circle(x,y,pen):
    screen_x = - (WIDTH/2.0) + 20 +x * 20
    screen_y = (HEIGHT/2.0) - 20 - y * 20
    pen.goto(screen_x, screen_y)
    pen.stamp()

picture = [
"r   ooo  yyy   ggg       bb    ppp  ooo  yyy  bbb",
"r    o    y    g         b b   p p   o    y   b",
"r    o    y    gg   www  bb    ppp   o    y   bb",
"r    o    y    g         b b   pp    o    y   b",
"rrr ooo   y    ggg       bb    p p  ooo   y   bbb",
]
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x,y,pen)
win.mainloop()