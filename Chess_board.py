import turtle
wn=turtle.Screen()
wn.setup(700,700)
q=turtle.Turtle('square')
q.hideturtle()
q.hideturtle()
q.shapesize(3)
q.color('black')
q.penup()
q.hideturtle()
q.goto(0,0)
turtle.tracer(2)
def condition(a,clr1,clr2):
    if j%2==0:
        q.color(clr1)
    else:
        q.color(clr2)
    q.goto(a+j*60,a+60*i)
    q.stamp()
    
for i in range(8):
    for j in range (8):
        if i%2==0:
            condition(-200,'coral','lightgray')
        if i%2>0:
            condition(-200,'lightgray','coral')
t=[]
im=['Rook.gif','Rook.gif','Knight.gif','Knight.gif','Bishop.gif',\
   'Bishop.gif','King.gif','Queen.gif','Pawn.gif','Pawn.gif','Pawn.gif','Pawn.gif',\
   'Pawn.gif','Pawn.gif','Pawn.gif','Pawn.gif',\
   'Rookw.gif','Rookw.gif','Knightw.gif','Knightw.gif','Bishopw.gif',\
   'Bishopw.gif','Kingw.gif','Queenw.gif','Pawnw.gif','Pawnw.gif','Pawnw.gif','Pawnw.gif',\
   'Pawnw.gif','Pawnw.gif','Pawnw.gif','Pawnw.gif'] 

for n in range (32):
    t.append(turtle.Turtle())
    wn.addshape(im[n])
    t[n].shape(im[n])
    t[n].penup()

t[0].goto(220,-200)
t[1].goto(-205,-200)
t[2].goto(-140,-200)
t[3].goto(160,-200)
t[4].goto(-85,-200)
t[5].goto(90,-200)
t[6].goto(-25,-200)
t[7].goto(40,-200)
for s in range (8,16):
    t[s].goto(-200+(s-8)*60,-140)
t[16].goto(220,220)
t[17].goto(-205,220)
t[18].goto(-140,220)
t[19].goto(160,220)
t[20].goto(-85,220)
t[21].goto(90,220)
t[22].goto(-25,220)
t[23].goto(40,220)
for s in range (24,32):
    t[s].goto(-200+(s-24)*60,160)

for n in range(32):
    t[n].ondrag(t[n].goto)
     


